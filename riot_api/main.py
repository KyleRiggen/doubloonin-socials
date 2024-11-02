from generate_final3_list import created_ranked_list
import json
import time as pause
from datetime import datetime
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

# def get_link():
#     load_dotenv('/Users/kyleriggenbach/Desktop/projects/doubloonin/config2.env')
#     username = os.environ['reddit_username']
#     password = os.environ['reddit_password']
#
#     driver = webdriver.Firefox()
#     driver.get("https://old.reddit.com/")
#
#     enter_username = driver.find_element(By.XPATH, '//*[@id="login_login-main"]/input[2]')
#     enter_password = driver.find_element(By.XPATH, '//*[@id="login_login-main"]/input[3]')
#     enter_username.send_keys(username)
#     enter_password.send_keys(password)
#     enter_password.send_keys(Keys.ENTER)
#
#     pause.sleep(5)
#     click_profile = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/span[1]/a')
#     click_profile.click()
#
#     submitted_tab = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/ul/li[3]/a')
#     submitted_tab.click()
#
#     desired_link = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[1]/div[2]/div[1]/p[1]/a')
#     link = desired_link.get_attribute('href')
#     return link


now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M")
print(formatted_time)

with open('/Users/kyleriggenbach/Desktop/projects/doubloonin-socials/riot_api/json/final3_list_keep.json') as user_file:
    file_contents = user_file.read()
final3_list = json.loads(file_contents)

data_import = created_ranked_list()


def publish_file2(data):
    now = datetime.now()
    f = open(f"publish-{formatted_time}.txt", "a")
    yesterday_link = 'https://www.reddit.com/r/leagueoflegends/comments/13m9f19/champion_performancepopularity_in_challengers/'
    meta_data = "__Champion Rank Points:__     \n" \
                "(highly subject to change)      \n" \
                "Picked +1 Point     \n" \
                "Banned +1 Point      \n" \
                "Won +2 Points     \n" \
                "Loss -2 Points     \n" \
                "&nbsp;     \n" \
                "     \n" \
                "__Star Player Points:__     \n" \
                "(highly subject to change)     \n" \
                "Kill +2 Points     \n" \
                "Death -2 Points     \n" \
                "Assist +1 Point     \n" \
                "&nbsp;     \n" \
                "     \n" \

    opening = f'||Champion|Points|Win % / Games Played|Rank Change from [Last Week]({yesterday_link})|Star Player| \n' \
              '|-|-|-|-|-|-| \n'
    f.write(meta_data)
    f.write(opening)

    for index, champ in enumerate(data):

        rank_value = abs(champ['rankChange'])
        if champ['rankChange'] > 0:
            rank_symbol = '🟩🔺'
        elif champ['rankChange'] < 0:
            rank_symbol = '🟥🔻'
        else:
            rank_symbol = '🟨'

        link_string_top = f"[{champ['topPlayer_name']}](https://www.op.gg/summoners/{champ['topPlayer_region']}/{champ['topPlayer_name']})"
        link_string_bot = f"[{champ['botPlayer_name']}](https://www.op.gg/summoners/{champ['botPlayer_region']}/{champ['botPlayer_name']})"

        if champ['topPlayer_name'] == '':
            link_string_top = 'not played'
            link_string_bot = ''
        elif champ['botPlayer_name'] == '':
            link_string_bot = ''

        string = f"| {index + 1} | {champ['champName']} | {champ['champScore']} |{champ['champWinPercent']} / {champ['champGames']}|{rank_symbol} {rank_value}| {link_string_top} |\n"
        string = string.rstrip()
        string += ' ' * 10
        f.write(string + '\n')

    f.close()


publish_file2(data_import)

# get_top_scores(new_champStats)
# get_top_player()
# create_publish_file()
