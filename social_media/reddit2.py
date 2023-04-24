from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
click_profile = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/span[1]/a')
click_profile.click()

submitted_tab = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/ul/li[3]/a')
submitted_tab.click()

desired_link = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[1]/div[2]/div[1]/p[1]/a')
link = desired_link.get_attribute('href')
print(link)

subreddit = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[3]/ul[2]/li[2]/a')
subreddit.click()

submit_text = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/a')
submit_text.click()

# time.sleep(1)
# submit_text_tab2 = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '/html/body/div[14]/div/div/div[2]/a[1]'))
# )
submit_text_tab = driver.find_element(By.XPATH, '/html/body/div[4]/form/ul/li[2]/a')
submit_text_tab.click()

# //*[@id="title-field"]/div/textarea
title_box = driver.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/div[2]/div[3]/div/div/textarea')
title_box.send_keys('this is a title scrapped')

# //*[@id="text-field"]/div/div/div/div[1]/textarea
text_box = driver.find_element(By.XPATH, '/html/body/div[4]/form/div[1]/div[2]/div[4]/div/div/div/div/div[1]/textarea')

text_string = ''
test_text = open("test.txt", "r")

while True:
    line = test_text.readline()
    if line == '': break
    text_string = text_string + line

test_text.close()
text_box.send_keys(text_string)

submit_post = driver.find_element(By.XPATH, '/html/body/div[4]/form/div[4]/button')
submit_post.click()

time.sleep(60)
driver.quit()