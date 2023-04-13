from setup import setup_enviorment
import json
import time

lol_watcher = setup_enviorment()
player_region = 'na1'

with open('json/puuid_list.json') as user_file:
    file_contents = user_file.read()
puuid_list_json = json.loads(file_contents)

print(puuid_list_json)
print(len(puuid_list_json))

match_list = []

for index, player in enumerate(puuid_list_json):
    matches = lol_watcher.match.matchlist_by_puuid(region=player_region, puuid=player, queue=420, start=0, count=5)
    if index >= 1:
        break
    print(index, matches)
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

for match in result:
    match_info = lol_watcher.match.by_id(region=player_region, match_id=match)['info']
    match_timestamp = match_info['gameStartTimestamp']
    converted_time = match_timestamp/1000
    print(time.ctime(converted_time))
