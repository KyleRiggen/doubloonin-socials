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

with open('champs.json') as user_file:
  file_contents = user_file.read()
champs_json = json.loads(file_contents)

lol_watcher = setup_enviorment()
player_region = 'na1'
queue_type = 'RANKED_SOLO_5x5'
challenger_ladder = lol_watcher.league.challenger_by_queue(region=player_region, queue=queue_type)

# get challenger ladder > receive summonerID
# convert summonerID to puuid (convert using summonerName)
# get matchIDs
# comb through matchIDs (remove duplicates)



# create array of 10 players only to look at
# workable_challenger_list = []
# count = 0
# for player in challenger_ladder['entries']:
#   workable_challenger_list.append(challenger_ladder['entries'][count]['summonerId'])
#   count = count + 1
#   if count >= 10:
#     break


# match_list = []
# for eachPlayer in workable_challenger_list:
#   # get match history
#   match = lol_watcher.match.matchlist_by_puuid(region=player_region, puuid=eachPlayer, queue=420, start=0, count=10)
#   print(match)

# get an array of matchIDs then check only the challenger players in those matches with their champ and KDA
# print(len(workable_challenger_list))





