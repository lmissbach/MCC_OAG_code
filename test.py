# this on the world bank to see if i can have my code tick boxes and download
# then I try on the OAG 
# test test 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Google Chrome version: 122.0.6261.129
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# The URL for the world bank data page 
#wbh_login_url = "https://datacatalog.worldbank.org/home"
wbd_login_url =  "https://datacatalog.worldbank.org/search?q=&sort=last_updated_date%20desc"

# Open the connect login page
driver.get(wbd_login_url)

#Open world bank data 
#menu_field = driver.find_element(By.CLASS_NAME, "fas fa-bars")# open menu with class fas fa-bars
# select data part 
#time.sleep(3)

# open triangle arrow with all the clickable things 
triangle_field = driver.find_element(By.CLASS_NAME, "triangle-arrow d-none d-md-block")
triangle_field.click()
# Find the label element that includes the text 'Afghanistan' and click it
#afghanistan_label = driver.find_element(By.XPATH, "//label[contains(., 'Afghanistan')]")
#afghanistan_label.click()

time.sleep(3)


#driver.quit()
# get the data page through class browse-popover
