import setup_api_stuff
from config_variables import *
import json
import time


with open('/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/riot_api/json/puuid_list_wRegion.json') as user_file:
    file_contents = user_file.read()
puuid_list_wRegion = json.loads(file_contents)

lol_watcher = setup_api_stuff.setup_enviorment()
match_list = []


def build_match_list():
    now = round(time.time())
    one_day = 86400
    one_week = (one_day * 7)
    few_days = (one_day * 3)
    one_day_ago = round(now - one_day)
    one_week_ago = round(now - one_week)
    few_days_ago = round(now - few_days)
    now_nice = time.ctime(time.time())

    for index, player in enumerate(puuid_list_wRegion):
        matches = lol_watcher.match.matchlist_by_puuid(region=player[1], puuid=player[0], queue=420, start=0, count=config['match_list']['match_count_per_player'], start_time=one_week_ago, end_time=now)

        if index >= config['match_list']['player_count']:
            break

        print(index, player, matches)
        for match in matches:
            combined = [match, player[1]]
            match_list.append(combined)

    print(match_list)

    isolated_region = 'na1'
    isolated_puuid = 'Wg394dzXL5rIr4pw87lXqVOaCCJ88e9Gpu-xNHSHhbKchnxFq6uIJ8AzL6_dmH-UyKftmvE_zDm7Qg'
    isolated_match_list = lol_watcher.match.matchlist_by_puuid(region=isolated_region, puuid=isolated_puuid, queue=420,
                                                               start=0, count=1)

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

    with open('/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/riot_api/json/match_list.json', 'w',
              encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    return result
