from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Google Chrome version: 122.0.6261.129
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# The URL for the hertie connect login page
connect_login_url = "https://connect.hertie-school.org/login/"

# credentials 
username = "giuliapetrilli2000@gmail.com"
password = "Hertie!!!2"

# Open the connect login page
driver.get(connect_login_url)

#time.sleep(3)

# Fill in the username and password
#username_field = driver.find_element(By.CLASS_NAME, "text span4 extralarge")
username_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email-address or username']")

#password_field = driver.find_element(By.CLASS_NAME, "password span4 extralarge")
password_field = driver.find_element(By.NAME, "loginpwd")

#time.sleep(3)
#username_field.send_keys(username + Keys.ENTER)
username_field.send_keys(username)
#time.sleep(3)
#password_field.send_keys(password + Keys.ENTER)
password_field.send_keys(password)
time.sleep(3)

# Click the login button - adjust the selector 
login_button = driver.find_element(By.LINK_TEXT, "Login")
login_button.click()
time.sleep(10)

# pause login process to complete
#time.sleep(10)

# navigating to the members page 
driver.get("https://connect.hertie-school.org/contact/")

# actual scraping starts here

# For example, scraping course information
#course_element = driver.find_element(By.CLASS_NAME, "coursename")
#print(course_element.text)

# Remember to quit the driver session when you're done
#time.sleep(10)
driver.quit()