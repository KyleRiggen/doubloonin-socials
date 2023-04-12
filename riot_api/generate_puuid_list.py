from riotwatcher import LolWatcher
from dotenv import load_dotenv
import os
import json

def setup_enviorment():
  load_dotenv('../config2.env')
  api_key = os.environ['riot_api_key']
  lol_watcher = LolWatcher(api_key)
  del(api_key)
  return lol_watcher

lol_watcher = setup_enviorment()
player_region = 'na1'
queue_type = 'RANKED_SOLO_5x5'
challenger_ladder = lol_watcher.league.challenger_by_queue(region=player_region, queue=queue_type)

count = 0
puuid_list = []

for index, player in enumerate(challenger_ladder['entries']):
  try:
    summoner_name = str(challenger_ladder['entries'][count]['summonerName'])
    puuid = lol_watcher.summoner.by_name(player_region, summoner_name)['puuid']
    puuid_list.append(puuid)
    print(count, index)
    count = count + 1
  except:
    print(f'error with name: {summoner_name}')
    count = count + 1

print(len(puuid_list))

with open('json/puuid_list.json', 'w', encoding='utf-8') as f:
    json.dump(puuid_list, f, ensure_ascii=False, indent=4)
