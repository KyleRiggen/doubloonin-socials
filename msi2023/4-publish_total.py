from datetime import datetime
import json

with open('/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/msi2023/jsons/2-total_stats.json') as user_file:
    file_contents = user_file.read()
data = json.loads(file_contents)

now = datetime.now()
formatted_time = now.strftime("%m-%d %H:%M")
f = open(f"publishes/total-{formatted_time}.txt", "a")

meta_data = "__Total Champion Rank Points:__     \n" \
            "(highly subject to change)      \n" \
            "Picked +1 Point     \n" \
            "Banned +1 Point      \n" \
            "Won +2 Points     \n" \
            "Loss -2 Points     \n" \
            "&nbsp;     \n" \
            "     \n"
opening = f'||Champion|Points| \n' \
          '|-|-|-| \n'
f.write(meta_data)
f.write(opening)

for index, champ in enumerate(data):
    string = f"| {index + 1} | {champ['name']} | {champ['score']} |\n"
    string = string.rstrip()
    string += ' ' * 10
    f.write(string + '\n')