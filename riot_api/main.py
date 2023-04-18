from doubloonin.riot_api.building_files.generate_final2_list import get_top_player
import json
import time

now_nice = time.ctime(time.time())
print(now_nice)

new_champStats = get_top_player()

# shipping json
with open('json/champ_stats.json', 'w', encoding='utf-8') as f:
    json.dump(new_champStats, f, ensure_ascii=False, indent=4)


# getting top 3 and sorting champs
def get_top_scores(champStats):
    list_champs = [(champStats[name]['champName'], champStats[name]['score']) for name in champStats]
    sorted_champs = sorted(list_champs, key=lambda x: x[1], reverse=True)
    print(f'list champs: ', list_champs)
    print('sorted champs: ', sorted_champs)
    # ret_dict = {}
    # for champ, kills in sorted_champs[:10]:
    #     ret_dict[champ] = kills

    return sorted_champs


def create_publish_file():
    f = open("publish.txt", "a")
    opening = '||Champion|Points|Top Player|Bottom Player| \n|-|-|-|-|-| \n'
    f.write(opening)

    for index, champ in enumerate(get_top_scores(new_champStats)):

        link_string_top = ''
        link_string_bottom = ''
        for bigChamp in new_champStats:

            if new_champStats[bigChamp]['champName'] == champ[0]:
                if len(new_champStats[bigChamp]['players']) == 1:
                    top_player_region = new_champStats[bigChamp]['players'][0][0]
                    top_player_name = new_champStats[bigChamp]['players'][0][1]
                    link_string_top = f'[{top_player_name}](https://www.op.gg/summoners/{top_player_region}/{top_player_name})'
                elif len(new_champStats[bigChamp]['players']) > 1:
                    bottom_player_region = new_champStats[bigChamp]['players'][-1][0]
                    bottom_player_name = new_champStats[bigChamp]['players'][-1][1]
                    link_string_bottom = f'[{bottom_player_name}](https://www.op.gg/summoners/{bottom_player_region}/{bottom_player_name})'

                    top_player_region = new_champStats[bigChamp]['players'][0][0]
                    top_player_name = new_champStats[bigChamp]['players'][0][1]
                    link_string_top = f'[{top_player_name}](https://www.op.gg/summoners/{top_player_region}/{top_player_name})'
                else:
                    link_string_top = 'not played'

        round_points = round(champ[1], 1)
        string = f"| {index + 1} | {champ[0]} | {round_points} | {link_string_top} | {link_string_bottom} |\n"
        f.write(string)

    f.close()


print(get_top_scores(new_champStats))
print(f'the um player function: {get_top_player()}')
create_publish_file()
