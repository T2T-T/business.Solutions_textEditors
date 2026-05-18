from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()

# Mouse controller
actions = ActionChains(driver)

# Website pages
pages_to_visit = [
    "https://professoro1.github.io/",
    "https://professoro1.github.io/create1.html",
]

# Visit pages
for page in pages_to_visit:
    driver.get(page)
    print("Visited:", page)
    time.sleep(2)

# Go to signup page
signup_page = "https://professoro1.github.io/create1.html"
driver.get(signup_page)

# Wait object
wait = WebDriverWait(driver, 10)

# Locate input fields
username_box = wait.until(
    EC.element_to_be_clickable((By.NAME, "Code Name"))
)

password_box = wait.until(
    EC.element_to_be_clickable((By.NAME, "Password"))
)

rapper_box = wait.until(
    EC.element_to_be_clickable((By.NAME, "What would your turtle rapper name be?"))
)

snack_box = wait.until(
    EC.element_to_be_clickable((By.NAME, "Favorite snack during a zombie apocalypse?"))
)

# Function to move mouse, click, and type
def mouse_click_and_type(element, text):
    actions.move_to_element(element).click().perform()
    time.sleep(0.5)

    element.clear()
    element.send_keys(text)

# Fill form using mouse clicks
mouse_click_and_type(username_box, "TurtleUser123")
mouse_click_and_type(password_box, "turtleuser@gmail.com")
mouse_click_and_type(rapper_box, "SuperPassword123")
mouse_click_and_type(snack_box, "Cookies")

time.sleep(1)

# Submit form
snack_box.send_keys(Keys.RETURN)

print("Account form submitted!")

time.sleep(3)

# Visit turtle page
turtle_page = ["https://professoro1.github.io/pages/turtles.html"
    "https://professoro1.github.io/create2.html",
    "https://professoro1.github.io/hello.html",
    "https://www.scrapethissite.com/pages/frames/?frame=i"
]
driver.get(turtle_page)

time.sleep(2)

# Find turtle names
turtle_elements = driver.find_elements(By.TAG_NAME, "li")

turtle_families = []

for turtle in turtle_elements:
    turtle_name = turtle.text.strip()

    if turtle_name:
        turtle_families.append(turtle_name)

# Print turtle families
print("\nTurtle Families:")
for family in turtle_families:
    print(family)

# Save to file
with open("turtle_families.txt", "w") as file:
    for family in turtle_families:
        file.write(family + "\n")

print("\nTurtle family names saved to turtle_families.txt")

time.sleep(5)

# Close browser
driver.quit()