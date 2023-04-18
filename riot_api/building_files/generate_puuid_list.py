from doubloonin.riot_api.building_files.setup import setup_enviorment
import json

lol_watcher = setup_enviorment()
player_region = ['na1', 'euw1', 'kr']
queue_type = 'RANKED_SOLO_5x5'
puuid_list_wRegion = []
puuid_list = []

for region in player_region:
    challenger_ladder = lol_watcher.league.challenger_by_queue(region=region, queue=queue_type)
    count = 0
    for index, player in enumerate(challenger_ladder['entries']):
        try:
            summoner_name = str(challenger_ladder['entries'][count]['summonerName'])
            puuid = lol_watcher.summoner.by_name(region, summoner_name)['puuid']
            region_code = region
            combined = (puuid, region_code)
            puuid_list_wRegion.append(combined)
            puuid_list.append(puuid)
            print(count, index, region)
            count = count + 1
        except:
            print(f'error with name: {summoner_name}')
            count = count + 1

print(len(puuid_list_wRegion))

with open('../json/puuid_list_wRegion.json', 'w', encoding='utf-8') as f:
    json.dump(puuid_list_wRegion, f, ensure_ascii=False, indent=4)

with open('../json/puuid_list.json', 'w', encoding='utf-8') as f:
    json.dump(puuid_list, f, ensure_ascii=False, indent=4)
