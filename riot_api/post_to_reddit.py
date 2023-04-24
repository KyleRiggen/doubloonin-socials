from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv('../config2.env')
USERNAME = os.environ['reddit_username']
PASSWORD = os.environ['reddit_password']
driver = webdriver.Firefox()

driver.get("https://old.reddit.com/")

enter_username = driver.find_element(By.XPATH, '//*[@id="login_login-main"]/input[2]')
enter_password = driver.find_element(By.XPATH, '//*[@id="login_login-main"]/input[3]')
enter_username.send_keys(USERNAME)
enter_password.send_keys(PASSWORD)
enter_password.send_keys(Keys.ENTER)

time.sleep(5)

subreddit = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[3]/ul[2]/li[2]/a')
subreddit.click()

submit_text = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/a')
submit_text.click()

submit_text_tab = driver.find_element(By.XPATH, '/html/body/div[4]/form/ul/li[2]/a')
submit_text_tab.click()

now_nice = time.ctime(time.time())
title_box = driver.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/div[2]/div[3]/div/div/textarea')
title_box.send_keys(f'this is a title scrapped {now_nice}')

text_box = driver.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/div[2]/div[4]/div/div/div/div/div[1]/textarea')

text_string = ''
test_text = open("test2.txt", "r")

while True:
    line = test_text.readline()
    if line == '': break
    text_box.send_keys(line)

test_text.close()
# text_box.send_keys(text_string)

submit_post = driver.find_element(By.XPATH, '/html/body/div[4]/form/div[4]/button')
submit_post.click()

time.sleep(60)
driver.quit()