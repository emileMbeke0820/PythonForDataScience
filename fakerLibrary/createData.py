from faker import Faker

fake = Faker()


def convert():
    for _ in range(5):
        fake.json(data_columns={'Spec': '@1.0.1', 'ID': 'pyint', 'Details': {'Name': 'name', 'Address': 'address'}},
                  num_rows=2)


def generateRandomMD5():
    for _ in range(5):
        print(fake.name())


if __name__ == '__main__':
    generateRandomMD5()
