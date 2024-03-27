from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

OAG_login_url = "https://analytics.oag.com/analyser-client/home"

# Open the OAG login page
driver.get(OAG_login_url)

# credentials 
username = "missbach@mcc-berlin.net"
password = "OAG#MCC#2023"

# Open the connect login page
driver.get(OAG_login_url)

# Fill in credentials 
username_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']")
password_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")

username_field.send_keys(username)
password_field.send_keys(password + Keys.ENTER)

# Go to Traffic Analyzer page 
traffic_analyser_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Traffic Analyser"))
)
traffic_analyser_link.click()

# Go to Power Table Report
power_table_report = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Power Table Report"))
)
power_table_report.click()

# Click Origin & Destination
origin_destination = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Destination"))
)
origin_destination.click()


# Click Average fare - Avg Fare
avg_fare = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Fare"))
)
avg_fare.click()

# Click Booking class 
booking_class = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Booking Class"))
)
booking_class.click()

# Select 

# Origin
# Country Albania (AL), 


#Destination
# country Croatia (HR), 

# Press the Run  <button title="" class="editButtons button button--cta">Run</button>

time.sleep(10)
driver.quit()