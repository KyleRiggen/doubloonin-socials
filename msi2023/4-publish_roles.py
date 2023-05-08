from datetime import datetime
import json


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
    opening = f'||{string.capitalize()} Champion|Points| \n' \
              '|-|-|-| \n'
    f.write(meta_data)
    f.write(opening)

    for index, champ in enumerate(data):

        print(champ)

        # top_totals[champ]['assists']

        string = f"| {index + 1} | {champ} | {data[champ]['score']} |\n"
        string = string.rstrip()
        string += ' ' * 10
        f.write(string + '\n')

publish_a_thing('top')
publish_a_thing('jungle')
publish_a_thing('mid')
publish_a_thing('bot')
publish_a_thing('sup')