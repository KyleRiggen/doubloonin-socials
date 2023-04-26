from bs4 import BeautifulSoup
import requests

response = requests.get(
    f'https://worldofwarcraft.blizzard.com/en-us/game/pvp/leaderboards/shuffle/deathknight/blood')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

main_html = soup.main
contents = main_html.child


print(contents.getText())

# /html/body/div[1]/div/main/div[3]/div[2]/div[7]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/a/div/div[2]
# /html/body/div[1]/div/main/div[3]/div[2]/div[7]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/a/div/div[2]
# /html/body/div[1]/div/main/div[3]/div[2]/div[7]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/a/div/div[2]










