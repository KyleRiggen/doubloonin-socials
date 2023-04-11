from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USERNAME = 'doubloonin'
PASSWORD = 'Paintball8!@#$'
driver = webdriver.Chrome()

driver.get("https://www.twitter.com/login")
try:
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
    time.sleep(5)
finally:
    driver.quit()

# def tweet_at_provider():
#     driver.get("https://www.reddit.com/")
#     time.sleep(2)
#     login = driver.find_element(By.XPATH, '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[2]/div/div[1]/a')
#     login.click()
#     time.sleep(2)
#     # justText = driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div/div/form/div[4]/a')
#     # print(justText.text)
#     # username = driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div/div/form/fieldset[1]/input')
#     # password = driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div/div/form/fieldset[2]/input')
#     # username.send_keys(USERNAME)
#     # password.send_keys(PASSWORD)
#     # time.sleep(2)
#     # password.send_keys(Keys.ENTER)
#     # time.sleep(60)
#
#
# tweet_at_provider()
