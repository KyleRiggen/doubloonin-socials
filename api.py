from riotwatcher import LolWatcher
from dotenv import load_dotenv
import os
import pandas as pd

lol_watcher = LolWatcher("RGAPI-3bee7ec3-2bbc-4a36-8c5d-84357d6465f2")

# for matchID in match_history:
#     match_data = lol_watcher.match.by_id(region=player_routing, match_id=matchID)
#     game_time = match_data['info']['gameDuration']
#     match_data2 = lol_watcher.match.by_id(region=player_routing2, match_id=matchID)['info']['gameDuration']


self_player_name = 'nykerion'
self_player_region = 'NA1'.lower()
self_player_routing = 'americas'
self_summoner = lol_watcher.summoner.by_name(self_player_region, self_player_name)
self_match_history = lol_watcher.match.matchlist_by_puuid(region=self_player_region, puuid=self_summoner['puuid'], queue=420, start=0, count=1)

print(self_summoner['puuid'])
print(self_match_history)

for matchID in self_match_history:
    match_data_0 = lol_watcher.match.by_id(region=self_player_routing, match_id=matchID)['info']

    for eachPerson in match_data_0['participants']:
        champ_name = eachPerson['championId']
        kills = eachPerson['kills']
        deaths = eachPerson['deaths']
        assists = eachPerson['assists']
        champ_score = (2*kills) + (assists) - (2*deaths)
        print(f"{champ_name} with a KDA of {kills}/{deaths}/{assists} and score of {champ_score}")

    for eachTeam in match_data_0['teams']:
        for eachBan in eachTeam['bans']:
            aBan = eachBan['championId']
            print(f"{aBan} has earned 5 points for being banned")
