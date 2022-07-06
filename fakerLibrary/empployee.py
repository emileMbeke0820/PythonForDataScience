# Import Faker
from faker import Faker
# Import JSON
import json

# Declare faker onject
fake = Faker()


# Define function to generate fake data and store into a JSON file
def generate_data(records):
    # Declare an empty dictionary
    customer = {}
    # Iterate the loop based on the input value and generate fake data
    for n in range(0, records):
        customer[n] = {}
        customer[n]['id'] = fake.random_number(digits=5)
        customer[n]['name'] = fake.name()
        customer[n]['address'] = fake.address()
        customer[n]['email'] = str(fake.email())
        customer[n]['phone'] = str(fake.phone_number())

    # Write the data into the JSON file
    with open('customer.json', 'w') as fp:
        json.dump(customer, fp)

    print("File has been created.")


# Take the number of records from the user
num = int(input("Enter the number of records:"))
# Call the function to generate fake records and store into a json file
generate_data(num)