from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://www.pokemon.com/us")

    driver.maximize_window()

    wait = WebDriverWait(driver, 15)
    actions = ActionChains(driver)

    # Wait for page to load
    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Open Pokédex page directly instead of hover navigation
    driver.get("https://www.pokemon.com/us/pokedex")

    # Search input
    search_bar = wait.until(
        EC.element_to_be_clickable((By.ID, "searchInput"))
    )

    search_bar.clear()
    search_bar.send_keys("Rayquaza")

    # Search button
    search_button = wait.until(
        EC.element_to_be_clickable((By.ID, "search"))
    )

    search_button.click()

    # Click Rayquaza card
    rayquaza_card = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h5[contains(text(),'Rayquaza')]")
        )
    )

    rayquaza_card.click()

    # Click Mega Rayquaza if available
    mega_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[contains(text(),'Mega Rayquaza')]")
        )
    )

    mega_button.click()

    print("Mega Rayquaza opened successfully!")

finally:
    driver.quit()
