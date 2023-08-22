import csv
from pathlib import Path

data_file_path = Path(__file__).resolve().parent / "hw14_adapter_proxy_pytest/task2/data.csv"


def add_row_to_csv(filename, row_data):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row_data)


def delete_row_from_csv(filename, row_index):
    rows = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows[:row_index] + rows[row_index + 1:])
