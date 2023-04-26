from bs4 import BeautifulSoup
import requests
import json

specs = ['Blood Death Knight', 'Frost Death Knight', 'Unholy Death Knight']
url_end = [
    'deathknight/blood',
    'deathknight/frost',
    'deathknight/unholy',
    'demonhunter/havoc',
    'demonhunter/vengeance',
    'druid/balance',
    'druid/feral',
    'druid/guardian',
    'druid/restoration',
    'evoker/devastation',
    'evoker/preservation',
    'hunter/beastmastery',
    'hunter/survival',
    'hunter/marksmanship',
    'mage/arcane',
    'mage/fire',
    'mage/frost',
    'monk/brewmaster',
    'monk/mistweaver',
    'monk/windwalker',
    'paladin/holy',
    'paladin/protection',
    'paladin/retribution',
    'priest/discipline',
    'priest/holy',
    'priest/shadow',
    'rogue/assassination',
    'rogue/outlaw',
    'rogue/subtlety',
    'shaman/elemental',
    'shaman/enhancement',
    'shaman/restoration',
    'warlock/affliction',
    'warlock/demonology',
    'warlock/destruction',
    'warrior/arms',
    'warrior/fury',
    'warrior/protection'
]
data2 = []

for spec_url in url_end:
    print(spec_url)

    response = requests.get(
        f'https://worldofwarcraft.blizzard.com/en-us/game/pvp/leaderboards/shuffle/{spec_url}')
    yc_web_page = response.text

    soup = BeautifulSoup(yc_web_page, 'html.parser')
    rows = soup.find(name='div', class_='SortTable-body')
    row_rows = rows.contents

    ratings = []
    for index, number in enumerate(row_rows):
        rating = row_rows[index].div.next_sibling.getText()
        ratings.append(rating)

    links = []
    for index, link in enumerate(row_rows):
        rating = row_rows[index].div.next_sibling.next_sibling.a.get('href')
        links.append(rating)

    character_names = []
    characters = soup.find_all(name='div', class_='Character-name')
    for index, toon in enumerate(characters):
        name_text = toon.getText()
        character_names.append(name_text)

    split_spec = spec_url.split('/')
    print(split_spec)

    for index, rating in enumerate(ratings):
        info = {
            'class_spec': spec_url,
            'class': split_spec[0].capitalize(),
            'spec': split_spec[1].capitalize(),
            'name': character_names[index],
            'rating': rating,
            'link': links[index],
        }
        data2.append(info)

print(data2)
print(len(data2))

sorted_data = sorted(data2, key=lambda x: int(x['rating']), reverse=True)

print(sorted_data)

# Open a file for writing
with open("jsons/output.json", "w") as outfile:
    # Convert the Python variable to JSON and write it to the file
    json.dump(sorted_data, outfile)