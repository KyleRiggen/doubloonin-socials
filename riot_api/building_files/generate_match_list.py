from doubloonin.riot_api.building_files.setup import setup_enviorment
import json
import time

with open('/Users/kyleriggenbach/Desktop/projects/doubloonin/riot_api/json/puuid_list_wRegion.json') as user_file:
    file_contents = user_file.read()
puuid_list_wRegion = json.loads(file_contents)

lol_watcher = setup_enviorment()
match_list = []
def build_match_list():

    now_nice = time.ctime(time.time())

    for index, player in enumerate(puuid_list_wRegion):
        matches = lol_watcher.match.matchlist_by_puuid(region=player[1], puuid=player[0], queue=420, start=0, count=5)
        if index >= 10:
            break

        print(index, player, matches)
        for match in matches:
            combined = [match, player[1]]
            match_list.append(combined)

    print(match_list)

    print(f'{now_nice} match list number before filtering duplicates: {len(match_list)}')
    # remove duplicated from list
    result = []
    for match in match_list:
        if match not in result:
            result.append(match)
        else:
            print(f'removed as a duplicate: {match}')

    now_nice = time.ctime(time.time())
    matches_to_go_over = len(result)
    print(f'{now_nice} match list number after filtering duplicates: {matches_to_go_over}')

    print(f'{now_nice} match list: {result}')
    return result