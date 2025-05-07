'''
A control module that demonstrates different use cases on the coordiMapper package.

'''
from coordiMapper.mapper import get_coordinates
import csv
import json

# User case 1. Get coordinates of a single location
location = 'John Fisher Junior Public School'
result = {location: get_coordinates(location)}
print(result)


# # User case 2. Read a .txt file with locations and get coordinates
# with open('./examples/locations.txt', 'r') as file:
#     locations = [line.strip() for line in file.readlines()]
#     coordinates = {loc: get_coordinates(loc, wait=0) for loc in locations}
#     [print(f"{loc}: {coord}") for loc, coord in coordinates.items()]

# # User case 3. Read a .csv file with locations and get coordinates
# with open('./examples/locations.csv', 'r') as file:
#     reader = csv.reader(file)
#     locations = [row[0].strip() for row in reader if row]  # Assuming locations are in the first column
#     coordinates = {loc: get_coordinates(loc, wait=0) for loc in locations}
#     [print(f"{loc}: {coord}") for loc, coord in coordinates.items()]
    

# User case 4. Read a .json file with locations and get coordinates
with open('./examples/locations.json', 'r') as file:
    data = json.load(file)
    locations = [school for district in data["locations"] for school in district["schools"]]
    coordinates = {loc: get_coordinates(loc, wait=0) for loc in locations}
    [print(f"{loc}: {coord}") for loc, coord in coordinates.items()]


