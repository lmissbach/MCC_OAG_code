# scrape from all airports in Denmark 

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

# Click Origin & Destination
origin_destination = driver.find_element(By.PARTIAL_LINK_TEXT, "Origin &")
origin_destination.click()

time.sleep(3)

# scroll don so the secment section is visible and recongizable by selenium 
python = driver.find_element(By.XPATH, '//*[@id="a-o-d"]')
driver.execute_script('arguments[0].scrollIntoView(true)', python)

#segment = driver.find_element(By.LINK_TEXT, "Segment")
#segment.click()

segment = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="radioSegment"]'))
)
segment.click()

# select country
country_box= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="id-Y-Country-airport1_include"]'))
)
country_box.click()

# Denmark 
# First, locate the element using the XPath
airport_origin_input = driver.find_element(By.XPATH, '//*[@id="airport1_include"]')

# Clear the input field in case there's any pre-filled text
airport_origin_input.clear()

# Enter the beginning or brandemburg airport to trigger the drop down menu 
airport_origin_input.send_keys('den')

# Wait for drop down menu options to show and then select berlin 
airport_origin = WebDriverWait(driver, 4).until(
    EC.element_to_be_clickable((By.ID, "ui-id-642"))
)
airport_origin.click()

# airport destination now
# First, locate the element using the XPath
airport_destination_input= driver.find_element(By.XPATH, '//*[@id="airport2_include"]')

# Clear the input field in case there's any pre-filled text
airport_destination_input.clear()

# insert any entry that will trigger a list, lo will give me a list of airports 
airport_destination_input.send_keys('lo')

# start by selecting the first element that has ui-id in its id, 
#download the report with that, 
# then go on to the next element with ui-id
# go on until the elements with ui-id are completed 





