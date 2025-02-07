import csv
import os
import configparser

# Load config.ini settings
config = configparser.ConfigParser()
config.read("config.ini")
CSV_FILE = config["REPORT"]["csv_file"]

# Initialize CSV file (write headers if file doesn't exist)
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Test Name", "Status", "Message"])  # CSV headers

# Append test results to CSV
def write_test_result(test_name, status, message):
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([test_name, status, message])

# Ensure CSV is initialized when module is imported
initialize_csv()
