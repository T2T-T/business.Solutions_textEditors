# Install Selenium first:
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Maximize window
driver.maximize_window()

# Wait helper
wait = WebDriverWait(driver, 15)

try:
    # 1) Go to the link
    driver.get("https://www.pokemon.com/us")

    # 2) Wait 2 seconds for the page to load
    time.sleep(2)

    # 3) Hover over the “Pokedex” link in the Navigation Bar
    pokedex_menu = wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, "Pokédex"))
    )

    ActionChains(driver).move_to_element(pokedex_menu).perform()

    # 4) Click on “Pokedex Hot List” link
    hot_list = wait.until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Hot List"))
    )

    hot_list.click()

    # Wait for page to load
    time.sleep(2)

    # Hover over the white search bar under name and number
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

    # Wait for search results
    time.sleep(2)

    # Click on "Rayquaza"
    rayquaza_result = wait.until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Rayquaza"))
    )

    rayquaza_result.click()

    # Wait 2 seconds
    time.sleep(2)

    # 5) On the Rayquaza page, click “Rayquaza”
    rayquaza_link = wait.until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Rayquaza"))
    )

    rayquaza_link.click()

    # Click “Mega Rayquaza”
    mega_rayquaza = wait.until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Mega Rayquaza"))
    )

    mega_rayquaza.click()

    # Wait 2 seconds
    time.sleep(2)

    # 6) Wait 5 seconds
    time.sleep(5)

finally:
    # Close browser
    driver.quit()