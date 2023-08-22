'''Напишіть адаптер, який конвертує json в csv'''

import csv
import json


class JsonToCsvConverter:
    def __init__(self):
        self.__data = []

    def read_file(self, filename: str):
        with open(filename, 'r') as json_file:
            self.__data = json.load(json_file)

    def write_to_file(self, filename: str):
        if self.__data:
            with open(filename, 'w', newline='') as csv_file:
                fieldnames = self.__data[0].keys()
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.__data)

    def cleanup(self):
        self.__data = []


json_to_csv_converter = JsonToCsvConverter()
json_to_csv_converter.read_file("users.json")
json_to_csv_converter.write_to_file("users_converted.csv")