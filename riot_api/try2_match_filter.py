from setup import setup_enviorment
import json
import time

now = time.time()
now_nice = time.ctime(time.time())
one_day = 86400
one_day_ago = now - one_day
print(now_nice)

lol_watcher = setup_enviorment()
player_region = 'na1'

with open('json/puuid_list.json') as user_file:
    file_contents = user_file.read()
puuid_list_json = json.loads(file_contents)

match_list = []

for index, player in enumerate(puuid_list_json):
    matches = lol_watcher.match.matchlist_by_puuid(region=player_region, puuid=player, queue=420, start=0, count=5)
    if index >= 20:
        break
    print(index, player, matches)
    for match in matches:
        match_list.append(match)

print(f'{now_nice} match list number before filtering duplicates: {len(match_list)}')
# remove duplicated from list
result = []
for match in match_list:
    if match not in result:
        result.append(match)
    else:
        print(f'removed as a duplicate: {match}')

print(result)
now_nice = time.ctime(time.time())
print(f'{now_nice} match list number after filtering duplicates: {len(result)}')

all_matches = []

for index, match in enumerate(result):
    match_info = lol_watcher.match.by_id(region=player_region, match_id=match)
    match_timestamp = match_info['info']['gameStartTimestamp']
    converted_time = match_timestamp / 1000

    now_nice = time.ctime(time.time())
    print(index, now_nice)

    player_list = []
    for player in match_info['info']['participants']:
        playerID = player['puuid']

        if playerID in puuid_list_json:
            player_dictionary = {
                'puuid': playerID,
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

now_nice = time.ctime(time.time())
print(f'{now_nice} match number after building custom dictionary: {len(all_matches)}')

all_matches_timed = []

for eachMatch in all_matches:
    viewableTime = time.ctime(eachMatch['gameStartTimestamp'])
    rawTime = eachMatch['gameStartTimestamp']
    if rawTime > one_day_ago:
        all_matches_timed.append(eachMatch)
        print(f'added: {viewableTime}')
    else:
        print(f'removed: {viewableTime}')

now_nice = time.ctime(time.time())
print(f'{now_nice} match number after filtering for time: {len(all_matches_timed)}')

final_results = {}
kills = 0
deaths = 0
assists = 0
for eachMatch in all_matches_timed:
    for eachPlayer in eachMatch['players']:

        champName = eachPlayer['champName']
        champKills = eachPlayer['kills']
        champDeaths = eachPlayer['deaths']
        champAssists = eachPlayer['assists']
        winBoolean = eachPlayer['win']

        if winBoolean == True:
            champWins = 1
            champLooses = 0
        else:
            champLooses = 1
            champWins = 0

        if champName not in final_results:
            final_results[champName] = {
                'kills': champKills,
                'deaths': champDeaths,
                'assists': champAssists,
                'champWins': champWins,
                'champLooses': champLooses
            }
        else:
            kills = final_results[champName]['kills'] + champKills
            deaths = final_results[champName]['deaths'] + champDeaths
            assists = final_results[champName]['assists'] + champAssists
            wins = final_results[champName]['champWins'] + champWins
            looses = final_results[champName]['champLooses'] + champLooses
            final_results[champName]['kills'] = kills
            final_results[champName]['deaths'] = deaths
            final_results[champName]['assists'] = assists
            final_results[champName]['champWins'] = wins
            final_results[champName]['champLooses'] = looses

now_nice = time.ctime(time.time())
print(f'{now_nice} champion entries into champ_stats.json: {len(final_results)}')

new_champStats = {}
for key, value in final_results.items():

    if key == 'MonkeyKing':
        new_key = 'Wukong'
    elif key == 'AurelionSol':
        new_key = 'Aurelion Sol'
    elif key == 'KSante':
        new_key = "K'Sante"
    elif key == 'JarvanIV':
        new_key = "Jarvan IV"
    else:
        new_key = key

    new_champStats[new_key] = value

with open('json/champ_stats.json', 'w', encoding='utf-8') as f:
    json.dump(new_champStats, f, ensure_ascii=False, indent=4)


