from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.maximize_window()

website_url = "https://professoro1.github.io/"
driver.get(website_url)

pages_to_visit = [
    "https://professoro1.github.io/",
    "https://professoro1.github.io/pages/page1.html",
    "https://professoro1.github.io/pages/page2.html",
    "https://professoro1.github.io/pages/page3.html",
    "https://professoro1.github.io/pages/page4.html"
]

for page in pages_to_visit:
    driver.get(page)
    print("Visited:", page)
    time.sleep(2)

signup_page = "https://professoro1.github.io/pages/signup.html"
driver.get(signup_page)

# Wait until username field appears
wait = WebDriverWait(driver, 10)

username_box = wait.until(
    EC.presence_of_element_located((By.ID, "username"))
)

email_box = driver.find_element(By.ID, "email")
password_box = driver.find_element(By.ID, "password")

username_box.send_keys("TurtleUser123")
email_box.send_keys("turtleuser@gmail.com")
password_box.send_keys("SuperPassword123")

time.sleep(1)

password_box.send_keys(Keys.RETURN)

print("Account form submitted!")

time.sleep(3)

turtle_page = "https://professoro1.github.io/pages/turtles.html"
driver.get(turtle_page)

time.sleep(2)

turtle_elements = driver.find_elements(By.TAG_NAME, "li")

turtle_families = []

for turtle in turtle_elements:
    turtle_name = turtle.text

    if turtle_name != "":
        turtle_families.append(turtle_name)

print("\nTurtle Families:")
for family in turtle_families:
    print(family)

with open("turtle_families.txt", "w") as file:
    for family in turtle_families:
        file.write(family + "\n")

print("\nTurtle family names saved to turtle_families.txt")

time.sleep(5)

driver.quit()