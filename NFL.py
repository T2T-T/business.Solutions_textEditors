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

#Acknoledge = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
#Acknoledge.click()

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

driver.get("https://www.ticketmaster.com/event/0F006482E67E7496?wt.mc_id=NFL_LEAGUE_SCHED_PG_SEA_LINK3&utm_source=NFL.com&utm_medium=client&utm_campaign=NFL_LEAGUE&utm_content=SCHED_PG_SEA_LINK3&campaign=sea-ti-iw-sp-2072738")
time.sleep(3)
