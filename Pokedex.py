from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# -----------------------------
# Setup Chrome WebDriver
# -----------------------------
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)
actions = ActionChains(driver)

try:
    # 1) Go to the link
    driver.get("https://www.marvelrivals.com")

    # 2) Wait 2 seconds for the page to load
    time.sleep(2)

    # --------------------------------------------------------
    # NOTE:
    # The following steps reference "Pokedex" and "Rayquaza",
    # which are NOT present on marvelrivals.com.
    # These selectors are placeholders and may need updating.
    # --------------------------------------------------------

    # 3) Hover over the “pokedex” link in the Navigation Bar
    pokedex_link = wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, "Pokedex"))
    )

    actions.move_to_element(pokedex_link).perform()

    # 4) Click on “pokedex hot list” link
    hot_list = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Pokedex Hot List"))
    )
    hot_list.click()

    # Hover over white search bar and type "Rayquaza"
    search_box = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input"))
    )

    actions.move_to_element(search_box).click().perform()

    search_box.clear()
    search_box.send_keys("Rayquaza")

    # Click the Rayquaza result
    rayquaza_result = wait.until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Rayquaza"))
    )
    rayquaza_result.click()

    # Wait 2 seconds
    time.sleep(2)

    # 5) On Rayquaza page, click “Rayquaza”
    rayquaza_page_link = wait.until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Rayquaza"))
    )
    rayquaza_page_link.click()

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


# ============================================
# NFL Stats Selenium Example
# ============================================

nfl_driver = webdriver.Chrome(options=options)

try:
    nfl_driver.get("https://www.nfl.com/stats/")

    # Wait until page loads
    WebDriverWait(nfl_driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    print("NFL stats page loaded successfully")
    print("Page Title:", nfl_driver.title)

    # Wait 5 seconds
    time.sleep(5)

finally:
    # Close NFL browser
    nfl_driver.quit()