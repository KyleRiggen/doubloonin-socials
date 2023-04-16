from doubloonin.riot_api.building_files.generate_working_list import build_working_list
import json

with open('/Users/kyleriggenbach/Desktop/projects/doubloonin/riot_api/json/champion.json') as user_file:
    file_contents = user_file.read()
champs_json = json.loads(file_contents)

all_matches_timed = build_working_list()

# building results dictionary
def buiding_final_list():
    # banned_champs = []
    #
    # champs_list = champs_json['data']
    # for match in all_matches_timed:
    #     # print(match['bans'])
    #     for index, champ in enumerate(champs_list):
    #         # print(champs_list[champ]['key'])
    #         if int(champs_list[champ]['key']) in match['bans']:
    #             banned_champs.append(champs_list[champ]['id'])
    #
    # print(f'banned CHAMPS!!! {banned_champs}')


    final_results = {}
    for eachMatch in all_matches_timed:

        for eachPlayer in eachMatch['players']:

            champName = eachPlayer['champName']
            champ_fixed_name = ''
            champKills = eachPlayer['kills']
            champDeaths = eachPlayer['deaths']
            champAssists = eachPlayer['assists']
            champVisionScore = eachPlayer['visionScore']
            winBoolean = eachPlayer['win']
            champID = 0

            if winBoolean:
                champWins = 1
                champLooses = 0
            else:
                champLooses = 1
                champWins = 0

            if champName in champs_json['data']:
                champID = champs_json['data'][champName]['key']
                champ_fixed_name = champs_json['data'][champName]['name']


            if champName not in final_results:

                final_results[champName] = {
                    'champName': champ_fixed_name,
                    'champID': champID,
                    'champStats': {
                        'kills': champKills,
                        'deaths': champDeaths,
                        'assists': champAssists,
                        'wins': champWins,
                        'losses': champLooses,
                        'visionScore': champVisionScore,
                        'bans': 0,
                        'picks': 0
                    }
                }

            else:
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

    # totaling scores
    for champ in final_results:
        score = 0
        score = score + (final_results[champ]['champStats']['kills'] * 3)
        score = score - (final_results[champ]['champStats']['deaths'] * 2)
        score = score + (final_results[champ]['champStats']['assists'] * 1)
        score = score + (final_results[champ]['champStats']['wins'] * 10)
        score = score - (final_results[champ]['champStats']['losses'] * 10)
        score = score + (final_results[champ]['champStats']['visionScore'] * 0.2)
        final_results[champ]['score'] = score

    return final_results
