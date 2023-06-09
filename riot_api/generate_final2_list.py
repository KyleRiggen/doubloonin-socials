from generate_final_list import building_final_list
import json

champStats = building_final_list()
def get_top_player():
    for champ in champStats:
        new_players = []
        for player in champStats[champ]['players']:
            found = False
            for player2 in new_players:
                if player2[1] == player[1]:
                    player2[2] += player[2]
                    found = True
                    break
            if not found:
                new_players.append(player)
        sorted_players = sorted(new_players, key=lambda x: x[2], reverse=True)

        champStats[champ]['players'] = sorted_players
        #print(f'added up new players to champ {champ}: {sorted_players}')

    with open('/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/riot_api/json/final2_list.json', 'w', encoding='utf-8') as f:
        json.dump(champStats, f, ensure_ascii=False, indent=4)

    return champStats