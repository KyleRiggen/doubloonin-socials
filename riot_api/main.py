from doubloonin.riot_api.building_files.generate_final3_list import created_ranked_list
import json
import time

now_nice = time.ctime(time.time())
print(now_nice)

with open('/Users/kyleriggenbach/Desktop/projects/doubloonin/riot_api/json/final3_list.json') as user_file:
    file_contents = user_file.read()
final3_list = json.loads(file_contents)

data_import = created_ranked_list()

def publish_file2(data):
    f = open(f"publish-{now_nice}.txt", "a")
    opening = '||Champion|Points|Best Player|Worst Player| \n|-|-|-|-|-| \n'
    f.write(opening)

    for index, champ in enumerate(data):

        link_string_top = f"[{champ['topPlayer_name']}](https://www.op.gg/summoners/{champ['topPlayer_region']}/{champ['topPlayer_name']})"
        link_string_bot = f"[{champ['botPlayer_name']}](https://www.op.gg/summoners/{champ['botPlayer_region']}/{champ['botPlayer_name']})"

        if champ['topPlayer_name'] == '':
            link_string_top = 'not played'
            link_string_bot = ''
        elif champ['botPlayer_name'] == '':
            link_string_bot = ''

        string = f"| {index + 1} | {champ['champName']} | {champ['champScore']} | {link_string_top} | {link_string_bot} |\n"
        f.write(string)

    f.close()

publish_file2(data_import)

# get_top_scores(new_champStats)
# get_top_player()
# create_publish_file()
