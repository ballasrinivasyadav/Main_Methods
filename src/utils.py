import csv
import os
import configparser

# # Load config.ini settings
# config = configparser.ConfigParser()
# config.read("config.ini")
# CSV_FILE = config["REPORT"]["csv_file"]

import configparser
import os

# Ensure config.ini exists
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../config.ini'))
if not os.path.exists(config_path):
    raise FileNotFoundError(f"Config file not found: {config_path}")

config = configparser.ConfigParser()
config.read(config_path)

# Debugging: Print all sections and keys
print("Config Sections:", config.sections())
for section in config.sections():
    print(f"[{section}]")
    for key, value in config[section].items():
        print(f"{key} = {value}")

# Now fetch the CSV file path
if "REPORT" in config:
    CSV_FILE = config["REPORT"].get("csv_file", "default_results.csv")  # Use default if missing
else:
    raise KeyError("'REPORT' section missing in config.ini")




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
