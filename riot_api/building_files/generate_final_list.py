from doubloonin.riot_api.building_files.generate_working_list import build_working_list
from doubloonin.riot_api.config_variables import *
import json

with open('/Users/kyleriggenbach/Desktop/projects/doubloonin/riot_api/json/champion.json') as user_file:
    file_contents = user_file.read()
champs_json = json.loads(file_contents)

all_matches_timed = build_working_list()


# building results dictionary
def building_final_list():

    banned_champs = []
    for match in all_matches_timed:
        # print(match['bans'])
        for index, champ in enumerate(champs_json['data']):
            # print(champs_list[champ]['key'])
            if int(champs_json['data'][champ]['key']) in match['bans']:
                banned_champs.append(champs_json['data'][champ]['id'])

    added_banned_champs = {}
    for champ in champs_json['data']:
        added_banned_champs[champ] = 0

    for champ in banned_champs:
        # addUp = 0
        if champ not in added_banned_champs.keys():
            added_banned_champs[champ] = 1
        else:
            addUp = added_banned_champs[champ] + 1
            added_banned_champs[champ] = addUp

    final_results = {}

    # starting the build
    for eachChamp in champs_json['data']:

        # cleaning up names
        if eachChamp in champs_json['data']:
            champID = champs_json['data'][eachChamp]['key']
            champ_fixed_name = champs_json['data'][eachChamp]['name']

        # adding in the players for each champ
        player_list = []
        for match in all_matches_timed:
            player_region = match['region']
            for player in match['players']:
                if player['champName'] == eachChamp:
                    player_list.append([player_region, player['summonerName'], player['playerScore']])
                elif player['champName'] == 'FiddleSticks' and eachChamp == 'Fiddlesticks':
                    player_list.append([player_region, player['summonerName'], player['playerScore']])

        final_results[eachChamp] = {
            'champName': champ_fixed_name,
            'champID': champID,
            'champStats': {
                'kills': 0,
                'deaths': 0,
                'assists': 0,
                'wins': 0,
                'losses': 0,
                'visionScore': 0,
                'picks': 0,
                'bans': added_banned_champs[eachChamp],
            },
            'players': player_list
        }

    for eachMatch in all_matches_timed:

        for eachPlayer in eachMatch['players']:

            champName = eachPlayer['champName']
            champKills = eachPlayer['kills']
            champDeaths = eachPlayer['deaths']
            champAssists = eachPlayer['assists']
            champVisionScore = eachPlayer['visionScore']
            winBoolean = eachPlayer['win']

            if winBoolean:
                champWins = 1
                champLooses = 0
            else:
                champLooses = 1
                champWins = 0

            kills = final_results[champName]['champStats']['kills'] + champKills
            deaths = final_results[champName]['champStats']['deaths'] + champDeaths
            assists = final_results[champName]['champStats']['assists'] + champAssists
            wins = final_results[champName]['champStats']['wins'] + champWins
            looses = final_results[champName]['champStats']['losses'] + champLooses
            visionScore = final_results[champName]['champStats']['visionScore'] + champVisionScore
            final_results[champName]['champStats']['kills'] = kills
            final_results[champName]['champStats']['deaths'] = deaths
            final_results[champName]['champStats']['assists'] = assists
            final_results[champName]['champStats']['wins'] = wins
            final_results[champName]['champStats']['losses'] = looses
            final_results[champName]['champStats']['visionScore'] = visionScore
            final_results[champName]['champStats']['picks'] += 1

    # totaling scores
    for champ in final_results:
        score = 0
        score = score + (final_results[champ]['champStats']['picks'] * config['points']['pick'])
        score = score + (final_results[champ]['champStats']['wins'] * config['points']['win'])
        score = score + (final_results[champ]['champStats']['losses'] * config['points']['loss'])
        score = score + (final_results[champ]['champStats']['bans'] * config['points']['ban'])
        final_results[champ]['score'] = score

    with open('/Users/kyleriggenbach/Desktop/projects/doubloonin/riot_api/json/final_list.json', 'w',
              encoding='utf-8') as f:
        json.dump(final_results, f, ensure_ascii=False, indent=4)

    return final_results
