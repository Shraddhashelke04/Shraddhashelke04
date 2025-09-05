# network-automation-vlans

This project uses [Netmiko](https://github.com/ktbyers/netmiko) to automate VLAN configuration on multiple Cisco switches.

## Requirements
- Python 3.10+
- Netmiko

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Setup
1. Update `devices.json` with your device IP addresses and credentials.
2. Ensure the devices are reachable from the machine running the script.

## Run
Execute the script to apply VLAN 10:

```bash
python vlan_config.py
```

The script connects to each device listed in `devices.json` and configures VLAN 10. If a device is unreachable or authentication fails, the error is printed and the script continues with the next device.
