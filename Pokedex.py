import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


try:
    driver.get("https://www.pokemon.com/us")
    driver.maximize_window()
    time.sleep(2)
    actions = ActionChains(driver)
    pokedex_nav = driver.find_element(By.CSS_SELECTOR, "a.explore")
    actions.move_to_element(pokedex_nav).perform() [cite: 106]
    time.sleep(1)
   
    hot_list_link = driver.find_element(By.LINK_TEXT, "Pokédex Hot List")
    hot_list_link.click() [cite: 104]
 
    search_bar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "searchInput"))
    )
    actions.move_to_element(search_bar).click().send_keys("Rayquaza").perform()
   
   
    search_button = driver.find_element(By.ID, "search")
    search_button.click()
    time.sleep(2)




    rayquaza_card = driver.find_element(By.XPATH, "//h5[text()='Rayquaza']")
    rayquaza_card.click()


    mega_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Mega Rayquaza')]"))
    )
    mega_button.click()
    time.sleep(2)


    time.sleep(5)


finally:
    driver.quit()
