from bs4 import BeautifulSoup
import requests

response = requests.get('https://old.reddit.com/user/KyleRiggen/submitted/')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

post_link = soup.find(name='a', class_='title may-blank')
# post_link_link = post_link.get('href')

print(soup)