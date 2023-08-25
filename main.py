import os,json,requests
from dotenv import load_dotenv

load_dotenv()
ETHERSNAN_API_KEY = os.getenv('ETHERSNAN_API_KEY')

# Ethereum address to monitor
target_address = "0x12476f5e2fde2f2b6179a8a884e4b53ab8fd6105"

# URL for fetching incoming transactions
url = f"https://api.etherscan.io/api?module=account&action=txlist&address={target_address}&sort=asc&apikey={ETHERSNAN_API_KEY}"

response = requests.get(url)
data = response.json()

if data["status"] == "1":
    incoming_transactions = data["result"]
    incoming_addresses = set(tx["from"] for tx in incoming_transactions)
    
    print("Incoming Addresses:")
    for address in incoming_addresses:
        print(address + "<br>")  # Add <br> tag for Markdown line break
        # Save the addresses to a JSON file
    with open("address.json", "w") as json_file:
        json.dump(list(incoming_addresses), json_file, indent=4)
else:
    print("API request failed.")