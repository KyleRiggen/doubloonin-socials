from matches import *
import json

with open('/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/riot_api/json/champion.json') as user_file:
    file_contents = user_file.read()
champs_json = json.loads(file_contents)

banned_champs = [];
added_banned_champs = []

for match in matches:
    for index, ban in enumerate(match['bans']):
        banned_champs.append(ban)

added_banned_champs = {}
for champ in champs_json['data']:
    added_banned_champs[champ] = banned_champs.count(champ)

# data = {k: v for k, v in added_banned_champs.items() if v != 0}

sorted_dict = dict(sorted(added_banned_champs.items(), key=lambda item: item[1], reverse=True))



with open('/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/msi2023/jsons/1-bans.json', 'w',
          encoding='utf-8') as f:
    json.dump(sorted_dict, f, ensure_ascii=False, indent=4)

print(len(sorted_dict))
print(sorted_dict)
