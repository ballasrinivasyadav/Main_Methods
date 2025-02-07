import pytest
from src.main import add, subtract
from src.utils import write_test_result  # Import CSV logging utility

def test_add_pass():
    """Test for addition function - should pass"""
    try:
        assert add(2, 3) == 5
        write_test_result("test_add_pass", "PASS", "Addition test passed")
    except AssertionError as e:
        write_test_result("test_add_pass", "FAIL", str(e))

def test_add_fail():
    """Test for addition function - should fail"""
    try:
        assert add(2, 3) == 6  # Intentional failure
        write_test_result("test_add_fail", "PASS", "Addition test passed")
    except AssertionError as e:
        write_test_result("test_add_fail", "FAIL", str(e))

def test_subtract_pass():
    """Test for subtraction function - should pass"""
    try:
        assert subtract(5, 3) == 2
        write_test_result("test_subtract_pass", "PASS", "Subtraction test passed")
    except AssertionError as e:
        write_test_result("test_subtract_pass", "FAIL", str(e))
