from matches import *
from config_variables import *
import json

with open('/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/msi2023/jsons/1-bans.json') as user_file:
    file_contents = user_file.read()
bans_json = json.loads(file_contents)

with open('/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/riot_api/json/champion.json') as user_file:
    file_contents = user_file.read()
champs_json = json.loads(file_contents)

results = []
for champ in champs_json['data']:

    champName = champs_json['data'][champ]['name']

    results.append({
        'name': champName,
        'picks': 0,
        'bans': bans_json[champ],
        'kills': 0,
        'deaths': 0,
        'assists': 0,
        'wins': 0,
        'losses': 0
    })


for match in matches:
    for pick in match['picks']:
        champName = pick['champ']
        champKills = pick['kills']
        champDeaths = pick['deaths']
        champAssists = pick['assists']
        winBoolean = pick['win']

        if winBoolean:
            champWins = 1
            champLooses = 0
        else:
            champLooses = 1
            champWins = 0

        for champ2 in results:
            if champName == champ2['name']:
                kills = champ2['kills'] + champKills
                deaths = champ2['deaths'] + champDeaths
                assists = champ2['assists'] + champAssists
                wins = champ2['wins'] + champWins
                losses = champ2['losses'] + champLooses

                champ2['kills'] = kills
                champ2['deaths'] = deaths
                champ2['assists'] = assists
                champ2['wins'] = wins
                champ2['losses'] = losses
                champ2['picks'] = champ2['picks'] + 1

for index, champ in enumerate(results):
    score = 0
    score = score + (results[index]['picks'] * config['points']['pick'])
    score = score + (results[index]['bans'] * config['points']['ban'])

    score = score + (results[index]['wins'] * config['points']['win'])
    score = score + (results[index]['losses'] * config['points']['loss'])

    # score = score + (results[index]['kills'] * config['points']['kill'])
    # score = score + (results[index]['deaths'] * config['points']['death'])
    # score = score + (results[index]['assists'] * config['points']['assist'])

    results[index]['score'] = score

print(len(results))
new_results = []
for champ in results:
    if champ['picks'] == 0 and champ['bans'] == 0:
        print(f'if block: name: {champ["name"]} picks: {champ["picks"]} bans: {champ["bans"]}')
    else:
        #print(f'else block: name: {champ["name"]} picks: {champ["picks"]} bans: {champ["bans"]}')
        new_results.append(champ)


sorted_list = sorted(new_results, key=lambda k: k['score'], reverse=True)
print(len(sorted_list))

with open('/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/msi2023/jsons/2-total_stats.json', 'w',
          encoding='utf-8') as f:
    json.dump(sorted_list, f, ensure_ascii=False, indent=4)



