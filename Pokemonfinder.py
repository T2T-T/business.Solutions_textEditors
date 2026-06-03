from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open Wikipedia
driver.get("https://www.wikipedia.org/")
time.sleep(2)

# Search for Pokemon
SearchBox = driver.find_element(By.ID, "searchInput")
SearchBox.send_keys("Pokemon")
SearchBox.send_keys(Keys.RETURN)
time.sleep(3)

# Create file for scraped data
file = open("PokemonData.txt", "w", encoding="utf-8")

# Page 1
Title1 = driver.find_element(By.ID, "firstHeading").text
file.write("PAGE 1\n")
file.write("Title: " + Title1 + "\n\n")

# Click Pikachu page
Pikachu = driver.find_element(By.PARTIAL_LINK_TEXT, "Pikachu")
Pikachu.click()
time.sleep(3)

# Page 2
Title2 = driver.find_element(By.ID, "firstHeading").text
file.write("PAGE 2\n")
file.write("Title: " + Title2 + "\n\n")

# Click Charizard page
Charizard = driver.find_element(By.PARTIAL_LINK_TEXT, "Charizard")
Charizard.click()
time.sleep(3)

# Page 3
Title3 = driver.find_element(By.ID, "firstHeading").text
file.write("PAGE 3\n")
file.write("Title: " + Title3 + "\n\n")

# Go back
driver.back()
time.sleep(2)

# Click Bulbasaur page
Bulbasaur = driver.find_element(By.PARTIAL_LINK_TEXT, "Bulbasaur")
Bulbasaur.click()
time.sleep(3)

# ---------------- PAGE 4 ----------------
Title4 = driver.find_element(By.ID, "firstHeading").text
file.write("PAGE 4\n")
file.write("Title: " + Title4 + "\n\n")

# Go back
driver.back()
time.sleep(2)

# Click Squirtle page
Squirtle = driver.find_element(By.PARTIAL_LINK_TEXT, "Squirtle")
Squirtle.click()
time.sleep(3)

# Page5
Title5 = driver.find_element(By.ID, "firstHeading").text
file.write("PAGE 5\n")
file.write("Title: " + Title5 + "\n\n")

# Scrape data
file.write("SCRAPED DATA\n")
file.write("-----------------\n")
file.write("1. " + Title1 + "\n")
file.write("2. " + Title2 + "\n")
file.write("3. " + Title3 + "\n")
file.write("4. " + Title4 + "\n")
file.write("5. " + Title5 + "\n\n")

# Scrape first 5 links from current page
Links = driver.find_elements(By.TAG_NAME, "a")

file.write("FIRST 5 LINKS FOUND:\n")

count = 0
for link in Links:
    href = link.get_attribute("href")

    if href:
        file.write(href + "\n")
        count += 1

    if count == 5:
        break

file.close()

print("Data saved to PokemonData.txt")

time.sleep(5)
driver.quit()