"""
Checkout Faker and create Fake Data for future use.
"""
import json

from faker import Faker

fake = Faker()

kunde = []


def createYourListe():
    for i in range(1, 20):
        i = fake.profile()
        kunde.append(i)

    return kunde


def write_to_json(dataset):
    with open('fakerLibrary/profile.json', 'w') as file:
        json.dump(dataset, file)


def readFile():
    with open("example.json", 'r') as file:
        print(file.read())


if __name__ == '__main__':
    dataset = {"child1": {"name": "Emil", "year": 2004},
  "child2": {"name": "Tobias", "year": 2007},
  "child3": {"name": "Linus", "year": 2011}}
    #print(createYourListe())
    write_to_json(dataset)
    #readFile()
