from doubloonin.riot_api.building_files.generate_working_list import build_working_list

all_matches_timed = build_working_list()

# building results dictionary
def buiding_final_list():
    final_results = {}
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

            if champName not in final_results:
                final_results[champName] = {
                    'kills': champKills,
                    'deaths': champDeaths,
                    'assists': champAssists,
                    'wins': champWins,
                    'losses': champLooses,
                    'visionScore': champVisionScore
                }
            else:
                kills = final_results[champName]['kills'] + champKills
                deaths = final_results[champName]['deaths'] + champDeaths
                assists = final_results[champName]['assists'] + champAssists
                wins = final_results[champName]['wins'] + champWins
                looses = final_results[champName]['losses'] + champLooses
                visionScore = final_results[champName]['visionScore'] + champVisionScore
                final_results[champName]['kills'] = kills
                final_results[champName]['deaths'] = deaths
                final_results[champName]['assists'] = assists
                final_results[champName]['wins'] = wins
                final_results[champName]['losses'] = looses
                final_results[champName]['visionScore'] = visionScore

    # cleaning up names
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
        elif key == 'XinZhao':
            new_key = "Xin Zhao"
        elif key == 'DrMundo':
            new_key = "Dr Mundo"
        elif key == 'KogMaw':
            new_key = "Kog'Maw"
        elif key == 'TahmKench':
            new_key = "Tahm Kench"
        else:
            new_key = key

        new_champStats[new_key] = value

    # totaling scores
    for champ in new_champStats:
        score = 0
        score = score + (new_champStats[champ]['kills'] * 3)
        score = score - (new_champStats[champ]['deaths'] * 2)
        score = score + (new_champStats[champ]['assists'] * 1)
        score = score + (new_champStats[champ]['wins'] * 10)
        score = score - (new_champStats[champ]['losses'] * 10)
        score = score + (new_champStats[champ]['visionScore'] * 0.2)
        new_champStats[champ]['score'] = score

    return new_champStats
