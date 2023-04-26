from bs4 import BeautifulSoup
import requests

specs = ['Blood Death Knight', 'Frost Death Knight', 'Unholy Death Knight']
url_end = ['deathknight/blood', 'deathknight/frost', 'deathknight/unholy']

character_list = []
character_names = []
character_points = []

character_collection = 90

for spec in url_end:
    response = requests.get(
        f'https://worldofwarcraft.blizzard.com/en-us/game/pvp/leaderboards/shuffle/{spec}')
    yc_web_page = response.text

    soup = BeautifulSoup(yc_web_page, 'html.parser')

    characters = soup.find_all(name='div', class_='Character-name')
    for index, toon in enumerate(characters):
        name_text = toon.getText()
        character_names.append(name_text)

    points_mid = []
    points_test_get = soup.find_all(name='div', class_='List')
    for index, point in enumerate(points_test_get):
        point_text = point.getText()
        points_mid.append(point_text)

    # points = [point.getText() for point in soup.find_all(name='div', class_='List')]
    points_mid = points_mid[7:]
    points_mid = points_mid[:100]

    for point in points_mid:
        character_points.append(point)

if len(character_names) < len(character_points):
    character_names.append('delete')


print(character_names)
print(len(character_names))

print(character_points)
print(len(character_points))

for index, person in enumerate(character_names):
    info = {
        'spec': 'Blood Death Knight',
        'name': person,
        'score': 0
    }
    character_list.append(info)

for index, point in enumerate(character_points):
    character_list[index]['score'] = point

print(character_list)