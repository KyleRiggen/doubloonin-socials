from riotwatcher import LolWatcher
from dotenv import load_dotenv
from filter_match_list import get_match_list
import os

def setup_enviorment():
  load_dotenv('../config2.env')
  api_key = os.environ['riot_api_key']
  lol_watcher = LolWatcher(api_key)
  del(api_key)
  return lol_watcher

lol_watcher = setup_enviorment()
player_region = 'na1'

match_list = get_match_list()
print(match_list)

for match in match_list:
  match_data = lol_watcher.match.by_id(region=player_region, match_id=match)['info']['participants']
  count = 0
  for player in match_data:
    print(match_data[count]['championName'])
    count = count + 1




