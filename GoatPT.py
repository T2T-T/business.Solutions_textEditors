from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)


driver.get("https://www.goat.com/")


JustDropped = driver.find_element(By.XPATH, '//*[@id="layout-wrapper"]/header[1]/header/nav/ul/li[2]/div[1]/a')
# 2. Initialize ActionChains
actions = ActionChains(driver)
actions.move_to_element(JustDropped)

actions.perform()
time.sleep(6)