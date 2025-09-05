import os
import sys
import pytest

# Ensure the parent directory is on the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import calculator


def test_add():
    assert calculator.add(2, 3) == 5


def test_subtract():
    assert calculator.subtract(5, 3) == 2


def test_multiply():
    assert calculator.multiply(4, 5) == 20


def test_divide():
    assert calculator.divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(1, 0)
