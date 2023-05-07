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

top_calc = []
for item in top:
    if item['champ'] not in top_calc:
        top_calc.append(item['champ'])

print(top_calc)