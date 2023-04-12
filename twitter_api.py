from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import config

USERNAME = config.twitter_username
PASSWORD = config.twitter_password
driver = webdriver.Chrome()

driver.get("https://www.twitter.com/login")

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"))
)
username.send_keys(USERNAME)
time.sleep(5)
username.send_keys(Keys.ENTER)
time.sleep(5)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"))
)
password.send_keys(PASSWORD)
time.sleep(5)
password.send_keys(Keys.ENTER)
time.sleep(60)

driver.quit()
