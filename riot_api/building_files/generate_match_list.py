from doubloonin.riot_api.building_files.setup import setup_enviorment
import json
import time

with open('/Users/kyleriggenbach/Desktop/projects/doubloonin/riot_api/json/puuid_list_wRegion.json') as user_file:
    file_contents = user_file.read()
puuid_list_wRegion = json.loads(file_contents)

lol_watcher = setup_enviorment()
match_list = []


def build_match_list():
    now = round(time.time())
    one_day = 86400
    one_day_ago = round(now - one_day)
    now_nice = time.ctime(time.time())

    for index, player in enumerate(puuid_list_wRegion):
        matches = lol_watcher.match.matchlist_by_puuid(region=player[1], puuid=player[0], queue=420, start=0, count=20, start_time=one_day_ago, end_time=now)

        # matches = lol_watcher.match.matchlist_by_puuid(region=player[1], puuid=player[0], queue=420, start=0, count=2)
        if index >= 300:
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

    with open('/Users/kyleriggenbach/Desktop/projects/doubloonin/riot_api/json/match_list.json', 'w',
              encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    return result
