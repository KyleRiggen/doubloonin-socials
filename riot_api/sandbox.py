data = [
    {
        'matchId': 'NA1_4628816391',
        'players': [
            {
                'champName': 'Gwen',
                'kills': 0,
                'deaths': 0,
            },
            {
                'champName': 'Rengar',
                'kills': 3,
                'deaths': 0,
            },
            {
                'champName': 'Morgana',
                'kills': 1,
                'deaths': 3,
            },
            {
                'champName': 'Ornn',
                'kills': 0,
                'deaths': 1,
            },
            {
                'champName': 'Sivir',
                'kills': 0,
                'deaths': 5,
            },
        ]
    },
    {
        'matchId': 'NA1_4628346281',
        'players': [
            {
                'champName': 'Rengar',
                'kills': 2,
                'deaths': 5,
            },
            {
                'champName': 'Sivir',
                'kills': 2,
                'deaths': 2,
            },
            {
                'champName': 'Ornn',
                'kills': 2,
                'deaths': 1,
            }
        ]
    },
    {
        'matchId': 'NA1_4628302501',
        'players': [
            {
                'champName': 'KSante',
                'kills': 0,
                'deaths': 2,
            },
            {
                'champName': 'Sivir',
                'kills': 1,
                'deaths': 2,
            }
        ]
    },
    {
        'matchId': 'NA1_4628254365',
        'players': [
            {
                'champName': 'Riven',
                'kills': 7,
                'deaths': 3,
            }
        ]
    }
]

final_results = {}
kills = 0
deaths = 0
for eachMatch in data:
    for eachPlayer in eachMatch['players']:

        champName = eachPlayer['champName']
        champKills = eachPlayer['kills']
        champDeaths = eachPlayer['deaths']

        if champName not in final_results:
            final_results[champName] = {'kills': champKills, 'deaths': champDeaths}
        else:
            kills = final_results[champName]['kills'] + champKills
            deaths = final_results[champName]['deaths'] + champDeaths
            final_results[champName]['kills'] = kills
            final_results[champName]['deaths'] = deaths

print(final_results)
print(len(final_results))
