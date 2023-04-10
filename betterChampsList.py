import json

with open('betterChamps.json') as user_file:
  file_contents = user_file.read()

parsed_json = json.loads(file_contents)

# id = '1'
# name = ''
# for person in parsed_json.values():
#     if person['id'] == id:
#         name = person['name']
# print(name)

ids = ['1', '3']
name = []

for id in ids:
    for person in parsed_json.values():
        if person['id'] == id:
            print(person['name'])
