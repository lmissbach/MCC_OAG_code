#from bs4 import BeautifulSoup
#import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#import time

# Google Chrome version: 122.0.6261.129

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://www.ilblast.it/")

input_element = driver.find_element(By.CLASS_NAME, "search-input") # this allows us to select the part in the html that we want to access 
input_element.send_keys("Ciao!" + Keys.ENTER)

time.sleep(10)
driver.quit()


#PATH = "C:\webdrivers\chromedriver-win64.exe"
#driver = webdriver.Chrome(PATH)





