from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Open Pokémon website
    driver.get("https://www.pokemon.com/us/pokedex")
    driver.maximize_window()

    wait = WebDriverWait(driver, 15)
    actions = ActionChains(driver)

    # -----------------------------
    # DEFINE SEARCH BAR + CLICK IT
    # -----------------------------
    search_bar = wait.until(
        EC.element_to_be_clickable((By.ID, "searchInput"))
    )

    search_bar.click()
    search_bar.clear()
    search_bar.send_keys("Rayquaza")

    # -----------------------------
    # DEFINE SEARCH BUTTON + CLICK IT
    # -----------------------------
    search_button = wait.until(
        EC.element_to_be_clickable((By.ID, "search"))
    )

    search_button.click()

    # -----------------------------
    # DEFINE RAYQUAZA CARD + CLICK IT
    # -----------------------------
    rayquaza_card = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h5[contains(text(),'Rayquaza')]")
        )
    )

    rayquaza_card.click()

    # -----------------------------
    # DEFINE MEGA RAYQUAZA BUTTON + CLICK IT
    # -----------------------------
    mega_rayquaza_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[contains(text(),'Mega Rayquaza')]")
        )
    )

    mega_rayquaza_button.click()

    print("Mega Rayquaza page opened successfully!")

    input("Press ENTER to close browser...")

finally:
    driver.quit()
