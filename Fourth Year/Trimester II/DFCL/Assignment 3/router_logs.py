import csv
from prettytable import PrettyTable

# Read the log file
with open('logs.csv', 'r') as log:

    # Parse as CSV
    router_logs = list(csv.reader(log))[1:]

    # Converting the parsed CSV into a proper table
    table = PrettyTable(['Sr.', 'Source', 'Destination', 'Protocol', 'Count'])
    for sr, row in enumerate(router_logs[1:]):
        table.add_row([sr+1, *row, router_logs.count(row)])

    # Printing the logs as a table
    print(table)