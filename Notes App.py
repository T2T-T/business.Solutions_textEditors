from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Open browser
driver = webdriver.Chrome()

# Open Wikipedia
driver.get("https://www.wikipedia.org/")
time.sleep(2)

# Search Pokemon
SearchBox = driver.find_element(By.ID, "searchInput")
SearchBox.send_keys("Pokemon")
SearchBox.send_keys(Keys.RETURN)
time.sleep(2)

# Open file
file = open("PokemonInfo.txt", "w")

# Data 1
Title1 = driver.find_element(By.ID, "firstHeading").text
file.write(Title1 + "\n")

# Page 2
Pikachu = driver.find_element(By.PARTIAL_LINK_TEXT, "Pikachu")
Pikachu.click()
time.sleep(2)

Title2 = driver.find_element(By.ID, "firstHeading").text
file.write(Title2 + "\n")

# Page 3
driver.get("https://en.wikipedia.org/wiki/Charizard")
time.sleep(2)

Title3 = driver.find_element(By.ID, "firstHeading").text
file.write(Title3 + "\n")

# Page 4
driver.get("https://en.wikipedia.org/wiki/Bulbasaur")
time.sleep(2)

Title4 = driver.find_element(By.ID, "firstHeading").text
file.write(Title4 + "\n")

# Page 5
driver.get("https://en.wikipedia.org/wiki/Squirtle")
time.sleep(2)

Title5 = driver.find_element(By.ID, "firstHeading").text
file.write(Title5 + "\n")

file.close()

time.sleep(5)
driver.quit()