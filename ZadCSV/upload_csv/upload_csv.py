import csv
import os

file_path = os.path.join(os.path.dirname(__file__), "ibook.csv")


def csv_writer():
    with open(file_path) as file:
        book = csv.reader(file)
        new_book = ""
        for row in book:
            new_book += ",".join(row) + "\n"
    return new_book


def csv_data():
    with open(file_path) as f:
        data = f.read().strip().split("\n")
    return data

print(csv_data())