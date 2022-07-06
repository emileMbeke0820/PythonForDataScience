import pandas as pd
import csv


def display_csv_reader():
    with open('monsters.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            print(row[1])


def display_csv_reader_dict():
    with open('monsters.csv', 'r') as file:
        dictReader = csv.DictReader(file, delimiter=',')
        for row in dictReader:
            print(row["monsterName"] + " is priced at " + row["price"])


def display_csv_pandas():
    df = pd.read_csv('monsters.csv')
    print(df)


if __name__ == '__main__':
    display_csv_pandas()
