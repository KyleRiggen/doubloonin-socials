from setup import setup_enviorment
import json
import time

lol_watcher = setup_enviorment()
player_region = 'na1'

with open('json/puuid_list.json') as user_file:
    file_contents = user_file.read()
puuid_list_json = json.loads(file_contents)

match_list = []

for index, player in enumerate(puuid_list_json):
    matches = lol_watcher.match.matchlist_by_puuid(region=player_region, puuid=player, queue=420, start=0, count=5)
    if index >= 4:
        break
    print(index, matches, player)
    for match in matches:
        match_list.append(match)

print(f'match list number:{len(match_list)}')
# remove duplicated from list
result = []
for match in match_list:
    if match not in result:
        result.append(match)
    else:
        print(f'removed as a duplicate: {match}')

print(result)
print(f'match list number:{len(result)}')

all_matches = []

for match in result:
    match_info = lol_watcher.match.by_id(region=player_region, match_id=match)
    match_timestamp = match_info['info']['gameStartTimestamp']
    converted_time = match_timestamp / 1000

    player_list = []
    for player in match_info['info']['participants']:
        player_dictionary = {
            'puuid': player['puuid'],
            'summonerName': player['summonerName'],
            'champID': player['championId'],
            'champName': player['championName'],
            'kills': player['kills'],
            'deaths': player['deaths'],
            'assists': player['kills'],
            'win': player['win']
        }

        # Add player dictionary to our player_list
        player_list.append(player_dictionary)

    match_dictionary = {
        'matchId': match_info['metadata']['matchId'],
        'gameStartTimestamp': converted_time,
        'players': player_list
    }

    all_matches.append(match_dictionary)

print(all_matches)
print(len(all_matches))

now = time.time()
one_day = 86400
one_day_ago = now - one_day
all_matches_timed = []

for eachMatch in all_matches:
    viewableTime = time.ctime(eachMatch['gameStartTimestamp'])
    rawTime = eachMatch['gameStartTimestamp']
    if rawTime > one_day_ago:
        all_matches_timed.append(eachMatch)
        print(f'added: {viewableTime}')
    else:
        print(f'removed: {viewableTime}')

print(all_matches_timed)
print(len(all_matches_timed))
