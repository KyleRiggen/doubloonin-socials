from generate_final2_list import get_top_player
import json
import time

data = get_top_player()
with open('/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/riot_api/json/final2_list.json') as user_file:
    file_contents = user_file.read()
final2_list = json.loads(file_contents)

with open('/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/riot_api/json/final3_list_keep.json') as user_file:
    file_contents = user_file.read()
yesterday = json.loads(file_contents)


def created_ranked_list():
    new_data = []
    for champ in data:
        champGames = data[champ]['champStats']['picks']

        if champGames != 0:
            champWinPercentage = round((data[champ]['champStats']['wins'] / champGames), 2)
        else:
            champWinPercentage = '-'

        champName = data[champ]['champName']
        champScore = round(data[champ]['score'], 1)

        if len(data[champ]['players']) == 1:
            topPlayer_name = data[champ]['players'][0][1]
            topPlayer_region = data[champ]['players'][0][0]
            botPlayer_name = ''
            botPlayer_region = ''
            if topPlayer_region == 'euw1':
                topPlayer_region = 'euw'
            elif topPlayer_region == 'na1':
                topPlayer_region = 'na'
        elif len(data[champ]['players']) > 1:
            topPlayer_name = data[champ]['players'][0][1]
            topPlayer_region = data[champ]['players'][0][0]
            botPlayer_name = data[champ]['players'][-1][1]
            botPlayer_region = data[champ]['players'][-1][0]
            if topPlayer_region == 'euw1':
                topPlayer_region = 'euw'
            elif topPlayer_region == 'na1':
                topPlayer_region = 'na'

            if botPlayer_region == 'euw1':
                botPlayer_region = 'euw'
            elif botPlayer_region == 'na1':
                botPlayer_region = 'na'
        else:
            topPlayer_name = ''
            topPlayer_region = ''
            botPlayer_name = ''
            botPlayer_region = ''

        new_data.append({

            'champName': champName,
            'champScore': champScore,
            'champGames': champGames,
            'champWinPercent': champWinPercentage,
            'topPlayer_name': topPlayer_name,
            'topPlayer_region': topPlayer_region,
            'botPlayer_name': botPlayer_name,
            'botPlayer_region': botPlayer_region
        })

    sorted_data = sorted(new_data, key=lambda x: x['champScore'], reverse=True)

    for index, champ in enumerate(sorted_data):

        champRank = index + 1
        sorted_data[index]['champRank'] = champRank
        rank_change = 0
        for index2, champ2 in enumerate(yesterday):
            if sorted_data[index]['champName'] == yesterday[index2]['champName']:
                rank_change = yesterday[index2]['champRank'] - sorted_data[index]['champRank']

        sorted_data[index]['rankChange'] = rank_change


    return sorted_data

# shipping json
now = round(time.time())
with open(f'/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/riot_api/json/final3_list_{now}.json', 'w', encoding='utf-8') as f:
    json.dump(created_ranked_list(), f, ensure_ascii=False, indent=4)

