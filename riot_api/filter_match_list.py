from riotwatcher import LolWatcher
from dotenv import load_dotenv
import os
import json
import time

def setup_enviorment():
  load_dotenv('../config2.env')
  api_key = os.environ['riot_api_key']
  lol_watcher = LolWatcher(api_key)
  del(api_key)
  return lol_watcher

with open('puuid_list.json') as user_file:
  file_contents = user_file.read()
puuid_list_json = json.loads(file_contents)

lol_watcher = setup_enviorment()
player_region = 'na1'

def get_match_list():

  # config numbers for API calls
  players_to_check = 3
  matches_to_check = 3

  # loop through the puuids to get a match list
  match_list = []
  for index, eachPlayer in enumerate(puuid_list_json):
    match = lol_watcher.match.matchlist_by_puuid(region=player_region, puuid=eachPlayer, queue=420, start=0, count=matches_to_check)
    print(index, match)
    for eachMatch in match:
      match_list.append(eachMatch)
    if (index + 1) >= players_to_check:
      break

  print(f'starting amount: {len(match_list)}')

  # remove duplicates
  match_list = list(dict.fromkeys(match_list))

  # remove old matches
  now = time.time()
  one_day = 86400
  one_day_ago = now - one_day
  new_match_list = []

  for match in match_list:
    match_timestamp = lol_watcher.match.by_id(region=player_region, match_id=match)['info']['gameStartTimestamp']
    converted_time = match_timestamp / 1000
    if converted_time > one_day_ago:
      new_match_list.append(match)
      print(f'adding: {time.ctime(converted_time)} < {time.ctime(one_day_ago)}')

  print(f'ending amount: {len(new_match_list)}')

  return new_match_list