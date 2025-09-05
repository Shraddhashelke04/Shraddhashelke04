import json
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetmikoTimeoutException, NetmikoAuthenticationException

def load_devices(filename: str):
    with open(filename) as f:
        return json.load(f)

def configure_vlan(device: dict, vlan_id: int) -> None:
    commands = [
        f"vlan {vlan_id}",
        f"name VLAN_{vlan_id}"
    ]
    connection = None
    try:
        connection = ConnectHandler(**device)
        connection.send_config_set(commands)
        print(f"{device['ip']}: VLAN {vlan_id} configured")
    finally:
        if connection:
            connection.disconnect()

def main():
    devices = load_devices('devices.json')
    for device in devices:
        try:
            configure_vlan(device, 10)
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            print(f"Failed to configure {device['ip']}: {error}")

if __name__ == "__main__":
    main()
