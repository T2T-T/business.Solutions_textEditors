from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)


driver.get("https://professoro1.github.io/")

# Website pages
CreateButton = driver.find_element(By.XPATH,"/html/body/div/button[1]")
CreateButton.click()
time.sleep(2)

CodeName = driver.find_element(By.ID, "codenameInput")
CodeName.send_keys("T2t")
time.sleep (1)

Password = driver.find_element(By.ID, "passwordInput")
Password.send_keys("1234567910")
time.sleep(1)

Rapper = driver.find_element(By.ID,"aiCantDoThis")
Rapper.send_keys("T2")
time.sleep(1)

Snacks = driver.find_element(By.ID, "mrOisSoSneaky")
Snacks.send_keys("Cookies")
time.sleep(1)

contiune = driver.find_element(By.XPATH, "/html/body/div/button")
contiune.click()
time.sleep(2)

Job = driver.find_element(By.ID,"pythonProgrammingIsCool")
Job.send_keys("Milk man")
time.sleep(1)

Pizza_topping = driver.find_element(By.ID,"security4")
Pizza_topping.send_keys("bacon")
time.sleep(1)

Mission = driver.find_element(By.ID,"security5")
Mission.send_keys("Spy")
time.sleep(1)


Power = driver.find_element(By.ID,"security6")
Power.send_keys("slow walk")

CreateAccount_button =driver.find_element(By.XPATH, "/html/body/div/button")
CreateAccount_button.click()
time.sleep(1)

Enter_turtle = driver.find_element(By.XPATH, "/html/body/button")
Enter_turtle.click()
time.sleep(2)

Cheloniidae = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/a")
Cheloniidae.click()

with open ("Turtlefile123.txt","w") as file: 
    file.write("Carettochelyidae, Cheloniidae, Chelydridae,Dermatemydidae, Dermochelyidae,Emydidae,Geoemydidae,Kinosternidae,Platysternidae,Testudinidae,Trionychidae, Chelidae,Pelomedusidae, Podocnemididae")


time.sleep(5)
driver.quit()


