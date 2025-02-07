import csv
import pytest
import sys
import os
from main import add

# Add project root to sys.path (to avoid ModuleNotFoundError)
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

# CSV file path
CSV_FILE = "test_results.csv"

# Prepare CSV headers
def write_csv_headers():
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Test Name", "Status", "Message"])  # Headers

# Append test results to CSV
def write_test_result(test_name, status, message):
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([test_name, status, message])

@pytest.fixture(scope="session", autouse=True)
def setup_csv():
    write_csv_headers()  # Initialize CSV file before running tests

def test_add_pass():
    """Test for addition function - expected to pass"""
    try:
        assert add(2, 3) == 5
        write_test_result("test_add_pass", "PASS", "Addition test passed")
    except AssertionError as e:
        write_test_result("test_add_pass", "FAIL", str(e))

def test_add_fail():
    """Test for addition function - expected to fail"""
    try:
        assert add(2, 3) == 6  # This will fail intentionally
        write_test_result("test_add_fail", "PASS", "Addition test passed")
    except AssertionError as e:
        write_test_result("test_add_fail", "FAIL", str(e))
