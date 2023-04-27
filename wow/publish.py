import json
from datetime import datetime

# Open the JSON file for reading
with open("jsons/output.json", "r") as infile:
    # Load the JSON data from the file into a Python object
    data = json.load(infile)

website = 'https://worldofwarcraft.blizzard.com'
now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M")
f = open(f"top100-{formatted_time}.txt", "a")

opening1 = '&nbsp;   \n'
opening2 = '__Top 100 Player and what they play__   \n'
opening3 = '               \n'
opening4 = '||Rating|Spec|Player| \n'
opening5 = '|-|-|-|-| \n'
f.write(opening1)
f.write(opening2)
f.write(opening3)
f.write(opening4)
f.write(opening5)

dps = '⚔️'
healer = '❤️‍🩹'

warlock = '🔮'  # purple globe thing
mage = '🧊'     # ice cube
shaman = '🔵'   # blue dot
death_knight = '🔴' # red dot
druid = '🟠'    # orange dot
warrior = '🟤️'  # brown dot
rogue = '🟡'    # yellow dot
monk = '🍺'     # beer mug
paladin = '🌸'  # pink flower
evoker = '🐉'   # green dragon
dh = '👿'       # purple demon face
hunter = '🦖'   # green dino
priest = '⚪'   # white dote

role_icon = ''
class_icon = ''

for index, item in enumerate(data):
    clas = data[index]['class']
    spec = data[index]['spec']
    name = data[index]['name']
    rating = data[index]['rating']
    link = data[index]['link']

    if spec in ('Restoration', 'Holy', 'Preservation', 'Mistweaver', 'Discipline'):
        role_icon = healer
    else:
        role_icon = dps

    if clas == 'Warlock':
        class_icon = warlock
    elif clas == 'Mage':
        class_icon = mage
    elif clas == 'Shaman':
        class_icon = shaman
    elif clas == 'Death Knight':
        class_icon = death_knight
    elif clas == 'Druid':
        class_icon = druid
    elif clas == 'Warrior':
        class_icon = warrior
    elif clas == 'Rogue':
        class_icon = rogue
    elif clas == 'Monk':
        class_icon = monk
    elif clas == 'Paladin':
        class_icon = paladin
    elif clas == 'Evoker':
        class_icon = evoker
    elif clas == 'Demon Hunter':
        class_icon = dh
    elif clas == 'Hunter':
        class_icon = hunter
    elif clas == 'Priest':
        class_icon = priest

    string = f'| {index + 1} | {rating} | {role_icon}{class_icon} {clas} {spec} | [{name}]({website}{link}) |'
    string = string.rstrip()
    string += ' ' * 10
    f.write(string + '\n')

f.close()

with open("jsons/summary.json", "r") as infile:
    summary_data = json.load(infile)

summary_file = open(f"summary-{formatted_time}.txt", "a")
opening1 = '__In the top 1000 of players, how much of each class/spec represented__      \n'
opening2 = '             \n'
opening3 = '|Specialization|Amount|     \n'
opening4 = '|-|-|     \n'
summary_file.write(opening1)
summary_file.write(opening2)
summary_file.write(opening3)
summary_file.write(opening4)

for key, value in summary_data.items():

    if key in (
            'Druid Restoration',
            'Paladin Holy',
            'Evoker Preservation',
            'Monk Mistweaver',
            'Priest Discipline',
            'Priest Holy',
            'Shaman Restoration',
    ):
        role_icon = healer
    else:
        role_icon = dps

    if 'Warlock' in key:
        class_icon = warlock
    elif 'Mage' in key:
        class_icon = mage
    elif 'Shaman' in key:
        class_icon = shaman
    elif 'Deathknight' in key:
        class_icon = death_knight
    elif 'Druid' in key:
        class_icon = druid
    elif 'Warrior' in key:
        class_icon = warrior
    elif 'Rogue' in key:
        class_icon = rogue
    elif 'Monk' in key:
        class_icon = monk
    elif 'Paladin' in key:
        class_icon = paladin
    elif 'Evoker' in key:
        class_icon = evoker
    elif 'Demonhunter' in key:
        class_icon = dh
    elif 'Hunter' in key:
        class_icon = hunter
    elif 'Priest' in key:
        class_icon = priest

    print(key)
    print(class_icon)

    string = f'|{role_icon}{class_icon} {key}|{value}|'
    string = string.rstrip()
    string += ' ' * 10
    summary_file.write(string + '\n')

summary_file.close()

# for key, value in sorted_dict.items():
#     words = key.split('/')
#     words = [word.capitalize() for word in words]
#     new_key = ' '.join(words)
#     cleaned[new_key] = value
