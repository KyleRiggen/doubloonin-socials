from riotwatcher import LolWatcher
from dotenv import load_dotenv
import os
import pandas as pd
import config
import json

with open('champs.json') as user_file:
  file_contents = user_file.read()

parsed_json = json.loads(file_contents)

lol_watcher = LolWatcher(config.riot_api_key)

# for matchID in match_history:
#     match_data = lol_watcher.match.by_id(region=player_routing, match_id=matchID)
#     game_time = match_data['info']['gameDuration']
#     match_data2 = lol_watcher.match.by_id(region=player_routing2, match_id=matchID)['info']['gameDuration']


self_player_name = 'DouyinTonyTop'
self_player_region = 'NA1'.lower()
self_player_routing = 'americas'
self_summoner = lol_watcher.summoner.by_name(self_player_region, self_player_name)
self_match_history = lol_watcher.match.matchlist_by_puuid(region=self_player_region, puuid=self_summoner['puuid'], queue=420, start=0, count=1)

print(self_summoner['puuid'])
print(self_match_history)

ban_ids = []

for matchID in self_match_history:
    match_data_0 = lol_watcher.match.by_id(region=self_player_routing, match_id=matchID)['info']

    for eachPerson in match_data_0['participants']:
        champ_id = eachPerson['championId']
        champ_name = eachPerson['championName']
        kills = eachPerson['kills']
        deaths = eachPerson['deaths']
        assists = eachPerson['assists']
        champ_score = (2*kills) + (assists) - (2*deaths)
        # print(f"{champ_name} ({champ_id}) with a KDA of {kills}/{deaths}/{assists} and score of {champ_score}")

    for eachTeam in match_data_0['teams']:
        for eachBan in eachTeam['bans']:
            aBan = str(eachBan['championId'])
            ban_ids.append(aBan)
            # print(f"{aBan} has earned 5 points for being banned")

for id in ban_ids:
    for person in parsed_json['data'].values():
        if person['key'] == id:
            print(person['name'])