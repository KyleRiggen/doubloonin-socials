from datetime import datetime
import json
from config_variables import *


def publish_a_thing(string):
    with open(f'/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/msi2023/jsons/2-roles_{string}.json') as user_file:
        file_contents = user_file.read()
    data = json.loads(file_contents)

    now = datetime.now()
    formatted_time = now.strftime("%m-%d %H:%M")
    f = open(f"publishes/5-{string}-{formatted_time}.txt", "a")

    meta_data = "__Role Champion Rank Points:__     \n" \
                "(highly subject to change)      \n" \
                "Kill +2 Points     \n" \
                "Death -2 Points      \n" \
                "Assist +1 Point     \n" \
                "&nbsp;     \n" \
                "     \n"
    opening = f'||{string.capitalize()} Champion|Points|Rank Change from [Yesterday]({config["yesterday_link"]})| \n' \
              '|-|-|-|-| \n'
    f.write(meta_data)
    f.write(opening)

    for index, champ in enumerate(data):

        rank_value = abs(data[champ]['rankChange'])
        if data[champ]['rankChange'] > 0:
            rank_symbol = '🟩🔺'
        elif data[champ]['rankChange'] < 0:
            rank_symbol = '🟥🔻'
        else:
            rank_symbol = '🟨'

        string = f"| {index + 1} | {champ} | {data[champ]['score']} | {rank_symbol} {rank_value}  | \n"
        string = string.rstrip()
        string += ' ' * 10
        f.write(string + '\n')

publish_a_thing('top')
publish_a_thing('jungle')
publish_a_thing('mid')
publish_a_thing('bot')
publish_a_thing('sup')


# for index, champ in enumerate(data):
#
#     rank_value = abs(champ['rankChange'])
#     if champ['rankChange'] > 0:
#         rank_symbol = '🟩🔺'
#     elif champ['rankChange'] < 0:
#         rank_symbol = '🟥🔻'
#     else:
#         rank_symbol = '🟨'
#
#     string = f"| {index + 1} | {champ['name']} | {champ['score']} | {rank_symbol} {rank_value} | \n"
#     string = string.rstrip()
#     string += ' ' * 10
#     f.write(string + '\n')