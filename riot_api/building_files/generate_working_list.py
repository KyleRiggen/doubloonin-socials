from doubloonin.riot_api.building_files.setup import setup_enviorment
from doubloonin.riot_api.building_files.generate_match_list import build_match_list
import time
import json

with open('/Users/kyleriggenbach/Desktop/projects/doubloonin/riot_api/json/puuid_list.json') as user_file:
    file_contents = user_file.read()
puuid_list = json.loads(file_contents)

now = time.time()
now_nice = time.ctime(time.time())
one_day = 86400
one_day_ago = now - one_day

lol_watcher = setup_enviorment()
result = build_match_list()
matches_to_go_over = len(result)
all_matches = []

# build dictionary of individual champion performance across all matches
def build_working_list():
    for index, match in enumerate(result):
        match_info = lol_watcher.match.by_id(region=match[1], match_id=match[0])
        match_timestamp = match_info['info']['gameStartTimestamp']
        match_duration = match_info['info']['gameDuration']
        converted_time = match_timestamp / 1000

        now_nice = time.ctime(time.time())
        print(f'{index} {now_nice} {match[0]} of {matches_to_go_over}')

        bans = []
        for teams in match_info['info']['teams']:
            for ban in teams['bans']:
                bans.append(ban['championId'])

        player_list = []
        for player in match_info['info']['participants']:
            playerID = player['puuid']

            if playerID in puuid_list:
                player_dictionary = {
                    'puuid': playerID,
                    'summonerName': player['summonerName'],
                    'champID': player['championId'],
                    'champName': player['championName'],
                    'kills': player['kills'],
                    'deaths': player['deaths'],
                    'assists': player['assists'],
                    'win': player['win'],
                    'visionScore': player['visionScore']
                }

                # Add player dictionary to our player_list
                player_list.append(player_dictionary)

        match_dictionary = {
            'matchId': match_info['metadata']['matchId'],
            'gameStartTimestamp': converted_time,
            'gameDuration': match_duration,
            'bans': bans,
            'players': player_list
        }

        all_matches.append(match_dictionary)

    now_nice = time.ctime(time.time())
    print(f'{now_nice} match number after building custom dictionary: {len(all_matches)}')

    all_matches_timed = []

    # filtering for time
    for eachMatch in all_matches:
        viewableTime = time.ctime(eachMatch['gameStartTimestamp'])
        rawTime = eachMatch['gameStartTimestamp']
        if rawTime > one_day_ago:
            all_matches_timed.append(eachMatch)
            print(f'added: {viewableTime}')
        else:
            print(f'removed: {viewableTime}')

    # filtering for remakes
    all_matches_finished = []
    for eachMatch in all_matches_timed:
        durationTime = eachMatch['gameDuration']
        if durationTime > 200:
            all_matches_finished.append(eachMatch)
            print(f'added: {durationTime}')
        else:
            print(f'removed: {durationTime}')

    now_nice = time.ctime(time.time())
    print(f'{now_nice} match number after filtering for time: {len(all_matches_finished)}')

    print(f'{now_nice} working list: {all_matches_finished}')
    return all_matches_finished
