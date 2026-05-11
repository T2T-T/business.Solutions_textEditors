from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


driver.maximize_window()


wait = WebDriverWait(driver, 15)

try:
   
    driver.get("https://www.pokemon.com/us")


    time.sleep(2)

    
    pokedex_menu = wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, "Pokédex"))
    )

    ActionChains(driver).move_to_element(pokedex_menu).perform()

  
    hot_list = wait.until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Hot List"))
    )

    hot_list.click()

    
    time.sleep(2)

    search_box = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[type='search']")
        )
    )

    ActionChains(driver).move_to_element(search_box).perform()

    # Type "Rayquaza"
    search_box.click()
    search_box.clear()
    search_box.send_keys("Rayquaza")

    time.sleep(2)

    rayquaza_result = wait.until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Rayquaza"))
    )

    rayquaza_result.click()

    time.sleep(2)

    rayquaza_link = wait.until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Rayquaza"))
    )

    rayquaza_link.click()

 
    mega_rayquaza = wait.until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Mega Rayquaza"))
    )

    mega_rayquaza.click()

    time.sleep(2)

    time.sleep(5)

finally:
    
    driver.quit()