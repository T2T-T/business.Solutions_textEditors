# pip install selenium webdriver-manager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Setup Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

wait = WebDriverWait(driver, 15)
actions = ActionChains(driver)

try:
    # Open website
    driver.get("https://professoro1.github.io/")

    # Click "Create Account"
    create_account_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[contains(text(),'Create Account')]")
        )
    )
    actions.move_to_element(create_account_btn).click().perform()

    # Fill Code Name
    code_name = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[contains(@placeholder,'Code') or contains(@name,'code')]")
        )
    )
    actions.move_to_element(code_name).click().perform()
    code_name.send_keys("T2")

    # Fill Password
    password = driver.find_element(
        By.XPATH,
        "//input[@type='password' or contains(@placeholder,'Password')]"
    )
    actions.move_to_element(password).click().perform()
    password.send_keys("password")

    # Security Question 1
    turtle_rapper = driver.find_element(
        By.XPATH,
        "//input[contains(@placeholder,'turtle rapper') or contains(@name,'rapper')]"
    )
    actions.move_to_element(turtle_rapper).click().perform()
    turtle_rapper.send_keys("T2T")

    # Security Question 2
    zombie_snack = driver.find_element(
        By.XPATH,
        "//input[contains(@placeholder,'zombie apocalypse') or contains(@name,'snack')]"
    )
    actions.move_to_element(zombie_snack).click().perform()
    zombie_snack.send_keys("pizza")

    # Click Continue
    continue_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[contains(text(),'Continue')]")
        )
    )
    actions.move_to_element(continue_btn).click().perform()

    # Cats ruled the world
    cats_world = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[contains(@placeholder,'cats ruled') or contains(@name,'cats')]")
        )
    )
    actions.move_to_element(cats_world).click().perform()
    cats_world.send_keys("Milk factory")

    pizza_topping = driver.find_element(
        By.XPATH,
        "//input[contains(@placeholder,'pizza topping') or contains(@name,'topping')]"
    )
    actions.move_to_element(pizza_topping).click().perform()
    pizza_topping.send_keys("bacon")


    turtle_mission = driver.find_element(
        By.XPATH,
        "//input[contains(@placeholder,'secret mission') or contains(@name,'mission')]"
    )
    actions.move_to_element(turtle_mission).click().perform()
    turtle_mission.send_keys("spy")

    superhero_power = driver.find_element(
        By.XPATH,
        "//input[contains(@placeholder,'superhero power') or contains(@name,'power')]"
    )
    actions.move_to_element(superhero_power).click().perform()
    superhero_power.send_keys("talking to fish")

    final_create_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[contains(text(),'Create Account')]")
        )
    )
    actions.move_to_element(final_create_btn).click().perform()


    enter_turtle_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[contains(text(),'Enter the Turtle')]")
        )
    )
    actions.move_to_element(enter_turtle_btn).click().perform()


    cheloniidae = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(),'Cheloniidae')]")
        )
    )

    actions.move_to_element(cheloniidae).perform()

    learn_more = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[contains(text(),'Learn More')]")
        )
    )
    actions.move_to_element(learn_more).click().perform()


    time.sleep(5)

finally:

    driver.quit()