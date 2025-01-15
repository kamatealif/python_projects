import csv

from prettytable import PrettyTable

def main():
    t_names = input("Enter the table names seprated with: ")
    table = PrettyTable(t_names.split())
    csv_file = 'demo.csv'
    with open(csv_file,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            table.add_row(row)
        print(table)

main()