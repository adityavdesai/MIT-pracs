#!/usr/bin/env python3

import csv
from prettytable import PrettyTable

log_file_name = 'wireshark_logs.csv'
print(f'Reading wireshark log file {log_file_name}!\n')

# Read the log file
with open(log_file_name, 'r') as file:
    # Create a table
    table = PrettyTable(['Frame Number', 'Frame Time', 'Source MAC', 'Destination MAC', 'Source IP', 'Destination IP', 'Protocol',])

    # Read all the logs and add to the table
    logs = list(csv.reader(file))
    for log in logs:
        table.add_row(log)

    print(table)
