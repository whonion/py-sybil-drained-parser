import csv
import json

def read_addresses_json(filename):
    with open(filename, 'r') as json_file:
        addresses = json.load(json_file)
    return addresses

def read_allocation_csv(filename):
    addresses = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row:
                addresses.append(row[0])
    return addresses

def compare_and_write_result(addresses_json, allocation_csv, output_filename):
    common_addresses = {}

    for address, incoming_addresses in addresses_json.items():
        common_incoming_addresses = set(incoming_addresses) & set(allocation_csv)
        if common_incoming_addresses:
            common_addresses[address] = list(common_incoming_addresses)

    with open(output_filename, 'w') as json_file:
        json.dump(common_addresses, json_file, indent=4)

if __name__ == "__main__":
    addresses_json_file = "addresses.json"
    allocation_csv_file = "allocation.csv"
    output_result_file = "sybil_result.json"

    addresses_json = read_addresses_json(addresses_json_file)
    allocation_csv = read_allocation_csv(allocation_csv_file)

    compare_and_write_result(addresses_json, allocation_csv, output_result_file)

    print("Comparison completed. Result written to", output_result_file)
