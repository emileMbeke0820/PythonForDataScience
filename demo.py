import json

import pandas as pan

from faker import Faker

ourFake = Faker()

ourProfile = [ourFake.profile() for i in range(20)]
ourDataFrame = pan.DataFrame(ourProfile)

with open('employee.json', 'w') as file:
    json.dump(ourProfile, file)

print(ourDataFrame)
