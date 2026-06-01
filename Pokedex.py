from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)


driver.get("https://www.nfl.com/")

Acknoledge = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
Acknoledge.click()

Games= driver.find_element(By.XPATH, '//*[@id="headlessui-popover-button-_R_6qb5kinpfdb_"]/span[1]')
# 2. Initialize ActionChains
actions = ActionChains(driver)
actions.move_to_element(Games)

actions.perform()
time.sleep(3)

Schedule = driver.find_element(By.XPATH, '//*[@id="headlessui-popover-panel-_R_aqb5kinpfdb_"]/ul/li[1]/div/ul/li[1]/a/span')
Schedule.click()
time.sleep(2)

Week1 =driver.find_element(By.XPATH, '//*[@id="headlessui-tabs-panel-_R_qld8ninpfdb_"]/div[1]/div[2]/div[1]/ul/li/div/a')
Week1.click()
time.sleep(2)

tabs = driver.window_handles
time.sleep(2)
driver.switch_to.window(tabs[1])
time.sleep(1)
Buy_Tickets = driver.find_element(By.XPATH,'//*[@id="ticket-card-a8fb0d78-4feb-11f1-abca-2c54536568a9"]/a')
Buy_Tickets.click()
time.sleep(2)