from riotwatcher import LolWatcher
import config
import json

with open('champs.json') as user_file:
  file_contents = user_file.read()
parsed_json = json.loads(file_contents)

lol_watcher = LolWatcher(config.riot_api_key)

self_player_name = 'DouyinTonyTop'
self_player_region = 'NA1'.lower()
self_player_routing = 'americas'
self_summoner = lol_watcher.summoner.by_name(self_player_region, self_player_name)
self_match_history = lol_watcher.match.matchlist_by_puuid(region=self_player_region, puuid=self_summoner['puuid'], queue=420, start=0, count=10)

champsDict = {}

for eachChamp in parsed_json['data'].values():
    champsDict[eachChamp['id']] = {'name': eachChamp['name'], 'score': None, 'id': parsed_json['data'][eachChamp['id']]['key']}

for matchID in self_match_history:
    match_data_0 = lol_watcher.match.by_id(region=self_player_routing, match_id=matchID)['info']

    for eachPerson in match_data_0['participants']:
        champ_id_pick = str(eachPerson['championId'])
        kills = eachPerson['kills']
        deaths = eachPerson['deaths']
        assists = eachPerson['assists']
        # champ_score = (2*kills) + (assists) - (2*deaths)
        # picked_ids.append(champ_id)
        for eachChamp_pick in champsDict.values():
            if eachChamp_pick['id'] == champ_id_pick:
                eachChamp_pick['score'] = + 2 + (kills) + (assists) - (deaths)
                # print(eachChamp_pick['score'], eachChamp_pick['name'])

    for eachTeam in match_data_0['teams']:
        for eachBan in eachTeam['bans']:
            champ_id_ban = str(eachBan['championId'])
            for eachChamp_ban in champsDict.values():
                if eachChamp_ban['id'] == champ_id_ban:
                    eachChamp_ban['score'] = +5
                    # print(eachChamp_ban['score'], eachChamp_ban['name'])

sortedDict = {}
for eachChamp in champsDict.values():
    if eachChamp['score'] is not None:
        sortedDict[eachChamp['name']] = eachChamp['score']

sorted_champs_by_score = sorted(sortedDict.items(), key=lambda x:x[1])
print(sorted_champs_by_score[-1])


