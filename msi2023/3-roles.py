from matches import *
from config_variables import *
import json

top = []
jungle = []
mid = []
bot = []
sup = []

for match in matches:
    for pick in match['picks']:
        if pick['position'] == 'top':
            top.append(pick)
        elif pick['position'] == 'jungle':
            jungle.append(pick)
        elif pick['position'] == 'mid':
            mid.append(pick)
        elif pick['position'] == 'bot':
            bot.append(pick)
        elif pick['position'] == 'sup':
            sup.append(pick)

def build_the_roles(array, name):
    top_totals = {}
    for item in array:
        champ = item['champ']
        kills = item['kills']
        deaths = item['deaths']
        assists = item['assists']
        if champ in top_totals:
            top_totals[champ]['kills'] += kills
            top_totals[champ]['deaths'] += deaths
            top_totals[champ]['assists'] += assists
        else:
            top_totals[champ] = {'kills': kills, 'deaths': deaths, 'assists': assists}

    for champ in top_totals:
        score = 0
        score = score + (top_totals[champ]['kills'] * config['points']['kill'])
        score = score + (top_totals[champ]['deaths'] * config['points']['death'])
        score = score + (top_totals[champ]['assists'] * config['points']['assist'])

        top_totals[champ]['score'] = score

    sorted_data = dict(sorted(top_totals.items(), key=lambda item: item[1]['score'], reverse=True))

    with open(f'/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/msi2023/jsons/2-roles_{name}.json', 'w',
              encoding='utf-8') as f:
        json.dump(sorted_data, f, ensure_ascii=False, indent=4)

build_the_roles(top, 'top')
build_the_roles(jungle, 'jungle')
build_the_roles(mid, 'mid')
build_the_roles(bot, 'bot')
build_the_roles(sup, 'sup')
