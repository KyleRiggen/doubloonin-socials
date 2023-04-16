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
driver = webdriver.Chrome()

driver.get("https://www.reddit.com/")

login = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[2]/div/div[1]/a'))
)
login.click()

driver.switch_to.frame(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[3]/div/div/iframe'))))

enter_username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="loginUsername"]'))
)
enter_password = driver.find_element(By.XPATH, '//*[@id="loginPassword"]')

enter_username.send_keys(USERNAME)
enter_password.send_keys(PASSWORD)
enter_password.send_keys(Keys.ENTER)

# //*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[1]/div[2]/button

time.sleep(60)
driver.quit()