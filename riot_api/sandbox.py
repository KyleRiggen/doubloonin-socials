import json

with open('/Users/kyleriggenbach/Desktop/projects/doubloonin/riot_api/json/working_list.json') as user_file:
    file_contents = user_file.read()
working_list = json.loads(file_contents)

data = [
    {
        "matchId": "KR_6455949298",
        "players": [
            {
                "champName": "Fiddlesticks",
                "win": False
            },
            {
                "champName": "Rakan",
                "win": True
            }
        ]
    },
    {
        "matchId": "KR_6455366349",
        "players": [
            {
                "champName": "FiddleSticks",
                "win": True
            },
            {
                "champName": "Rakan",
                "win": True
            },
            {
                "champName": "FiddleSticks",
                "win": False
            },
            {
                "champName": "Rakan",
                "win": True
            },
            {
                "champName": "Fiddlesticks",
                "win": False
            }
        ]
    }
]

final_results = {
    "Fiddlesticks": {
        "champName": "Fiddlesticks",
        "champID": "266",
        "champStats": {
            "wins": 0,
            "losses": 0,
        },
    },
    "FiddleSticks": {
        "champName": "FiddleSticks",
        "champID": "266",
        "champStats": {
            "wins": 0,
            "losses": 0,
        },
    },
    "Rakan": {
        "champName": "Rakan",
        "champID": "103",
        "champStats": {
            "wins": 0,
            "losses": 0,
        },
    }
}
count = 0
for match in working_list:

    for player in match['players']:
        winBoolean = player['win']
        champName = player['champName']

        count = count + 1
        # print(count)
        if champName == 'FiddleSticks' or champName == 'Fiddlesticks':
            print('hi', champName)
            champName = 'Fiddlesticks'

        if winBoolean:
            champWins = 1
            champLooses = 0
        else:
            champLooses = 1
            champWins = 0

        wins = final_results[champName]['champStats']['wins'] + champWins
        looses = final_results[champName]['champStats']['losses'] + champLooses
        final_results[champName]['champStats']['wins'] = wins
        final_results[champName]['champStats']['losses'] = looses

print(final_results)




# data['matchId']['champName'] == 'FiddleSticks'
