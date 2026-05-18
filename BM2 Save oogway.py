from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()

# Website pages
pages_to_visit = [
    "https://professoro1.github.io/",
    "https://professoro1.github.io/create1.html",
    "https://professoro1.github.io/create2.html",
    "https://professoro1.github.io/hello.html",
    "https://www.scrapethissite.com/pages/frames/?frame=i"
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

# Locate elements
username_box = wait.until(
    EC.element_to_be_clickable((By.NAME, "username"))
)

email_box = wait.until(
    EC.element_to_be_clickable((By.NAME, "email"))
)

password_box = wait.until(
    EC.element_to_be_clickable((By.NAME, "password"))
)

snack_box = wait.until(
    EC.element_to_be_clickable((By.NAME, "snack"))
)

# Click and type into username
username_box.click()
username_box.clear()
username_box.send_keys("TurtleUser123")

# Click and type into email
email_box.click()
email_box.clear()
email_box.send_keys("turtleuser@gmail.com")

# Click and type into password
password_box.click()
password_box.clear()
password_box.send_keys("SuperPassword123")

# Click and type into snack field
snack_box.click()
snack_box.clear()
snack_box.send_keys("Cookies")

time.sleep(1)

# Submit form
password_box.send_keys(Keys.RETURN)

print("Account form submitted!")

time.sleep(3)

# Visit turtle page
turtle_page = "https://professoro1.github.io/pages/turtles.html"
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