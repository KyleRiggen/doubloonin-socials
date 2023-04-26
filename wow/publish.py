import json
from datetime import datetime

# Open the JSON file for reading
with open("jsons/output.json", "r") as infile:
    # Load the JSON data from the file into a Python object
    data = json.load(infile)

# Print the Python object to verify that the data was loaded correctly
print(data)

now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M")
f = open(f"publish-{formatted_time}.txt", "a")
opening = '||Rating|Spec|Player| \n'
opening2 = '|-|-|-|-| \n'
f.write(opening)
f.write(opening2)

for index, item in enumerate(data):
    spec = data[index]['spec']
    name = data[index]['name']
    rating = data[index]['rating']

    string = f'| {index + 1} | {rating} | {spec} | {name} |'
    string = string.rstrip()
    string += ' ' * 10
    f.write(string + '\n')

f.close()

# string = f"| {index + 1} | {champ['champName']} | {champ['champScore']} |{rank_symbol} {rank_value}| {link_string_top} |\n"
# string = string.rstrip()
# string += ' ' * 10
# f.write(string + '\n')