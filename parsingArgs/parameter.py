from faker import Faker
import json

fake = Faker()


def peopleData(person):
    kunde = []
    for name, email in person:
        kunde.append("a: {},{}".format(name, email))
    return kunde


if __name__ == '__main__':
    name = fake.name()
    email = fake.email()
    print(json.dumps(peopleData([(name, email)])))
