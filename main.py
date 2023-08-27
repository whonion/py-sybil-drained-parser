import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
ETHERSNAN_API_KEY = os.getenv('ETHERSNAN_API_KEY')

def fetch_incoming_transactions(target_address):
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={target_address}&sort=asc&apikey={ETHERSNAN_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "1":
        incoming_transactions = data["result"]
        incoming_addresses = [tx["from"] for tx in incoming_transactions]
        return incoming_addresses
    else:
        print(f"API request failed for address: {target_address}")
        return []

# Load target addresses from scammers.txt
target_addresses = []
with open("scammers.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            target_addresses.append(line)

# Load existing data from addresses.json if it exists
existing_data = {}
if os.path.exists("addresses.json"):
    with open("addresses.json", "r") as json_file:
        existing_data = json.load(json_file)

# Fetch and append incoming addresses for each target address
for target_address in target_addresses:
    incoming_addresses = fetch_incoming_transactions(target_address)
    existing_data[target_address] = incoming_addresses

# Write the updated data to addresses.json
with open("addresses.json", "w") as json_file:
    json.dump(existing_data, json_file, indent=4)

print("Results appended to addresses.json.")
