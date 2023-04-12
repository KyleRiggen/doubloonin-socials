import json

puuid_list_list = ['1', '2', '3', '4']

with open('puuid_list.json', 'w', encoding='utf-8') as f:
    json.dump(puuid_list_list, f, ensure_ascii=False, indent=4)