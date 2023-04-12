from riotwatcher import LolWatcher
from dotenv import load_dotenv
from filter_match_list import get_match_list
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

with open('json/puuid_list.json') as user_file:
  file_contents = user_file.read()
puuid_list_json = json.loads(file_contents)

big_dict = {}

match_list = get_match_list()
print(match_list)

for match in match_list:
  match_data = lol_watcher.match.by_id(region=player_region, match_id=match)['info']['participants']
  count = 0
  for index, player in enumerate(match_data):
    player_puuid = match_data[count]['puuid']
    player_name = match_data[count]['summonerName']
    champ_name = match_data[count]['championName']
    champ_id = match_data[count]['championId']
    champ_kills = match_data[count]['kills']
    champ_deaths = match_data[count]['deaths']
    champ_assists = match_data[count]['assists']
    champ_win = match_data[count]['win']
    print(match_data[count]['championName'], player_puuid)
    for goodPuuid in puuid_list_json:
      if goodPuuid == player_puuid:
        big_dict[player_puuid] = {
          'puuid': player_puuid,
          'playerName': player_name,
          'champ_name': champ_name,
          'champ_id': champ_id,
          'kills': champ_kills,
          'deaths': champ_deaths,
          'assists': champ_assists,
          'win': champ_win
        }
    count = count + 1


#   for index, eachPlayer in enumerate(puuid_list_json):
print(big_dict)
print(len(big_dict))





