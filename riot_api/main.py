from doubloonin.riot_api.building_files.generate_final_list import buiding_final_list
import json
import time

now_nice = time.ctime(time.time())
print(now_nice)

new_champStats = buiding_final_list()

# shipping json
with open('json/champ_stats.json', 'w', encoding='utf-8') as f:
    json.dump(new_champStats, f, ensure_ascii=False, indent=4)


# getting top 3 and sorting champs
def get_top_scores(champStats):
    list_champs = [(name, champStats[name]['score']) for name in champStats]
    sorted_champs = sorted(list_champs, key=lambda x: x[1], reverse=True)
    # print(sorted_champs)
    ret_dict = {}
    for champ, kills in sorted_champs[:10]:
        ret_dict[champ] = kills

    return sorted_champs
def create_publish_file():
    f = open("publish.txt", "a")
    opening = '||Champion|Points| \n|-|-|-| \n'
    f.write(opening)

    for index, champ in enumerate(get_top_scores(new_champStats)):
        round_points = round(champ[1], 1)
        string = f"| {index + 1} | {champ[0]} | {round_points} | \n"
        f.write(string)

    f.close()

print(get_top_scores(new_champStats))
create_publish_file()
