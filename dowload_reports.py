from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Set the download directory - change
download_directory = r"H:\6_Coupled Goods\2_Data\OAG data" # This is my folder, you have to change it to yours 

service = Service(executable_path="chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", { # this tells the browser to download the files in the specified folder
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
})
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 5)


def login(): # this function logs in to the OAG website
    OAG_login_url = "https://analytics.oag.com/analyser-client/home"
    driver.get(OAG_login_url)
    username = "missbach@mcc-berlin.net"
    password = "OAG#MCC#2023"
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(password + Keys.ENTER)


def navigate_to_job_bin(): # this function navigates to the job bin page
    traffic_analyser_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Traffic Analyser")))
    traffic_analyser_link.click()
    my_oag = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div/nav/ul/li[2]/a')))
    my_oag.click()
    job_bin =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div/nav/ul/li[2]/ul/li[3]/a')))
    job_bin.click()
    time.sleep(4)

def select_50_reports(): # this function selects 50 reports per page, so that we can download more reports at once
    select = driver.find_element(By.XPATH, '//*[@id="pageSizeOptions"]/option[3]')
    select.click()
    time.sleep(10)


def download(): # this function downloads the reports
    # Locate the table by its XPath and find all 'a' elements with href attributes within it
    table_xpath = '//*[@id="job-bin-container"]/div/div[1]/table' # this is the xpath of the table in the job bin
    links = driver.find_elements(By.XPATH, f'{table_xpath}//a[@href]')

    # Iterate over each link and click it
    for link in links:
        href = link.get_attribute('href') 
        print(f'Clicking on: {href}')  # Printing the href for your reference
        time.sleep(2)
        driver.execute_script("arguments[0].click();", link) # Clicking the link using JavaScript
        time.sleep(2)  # Adding a delay between clicks to prevent server overload or being flagged as a bot


def main():
    login()  # Initial login
    navigate_to_job_bin()

def main_1():
    select_50_reports()
    download()
       
if __name__ == "__main__":
    main()
    # Goal: Repeat this 17 times --> clicking on new page and downloading 50 files
    for n in range(17):
        main_1()
        click_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div/table/tbody/tr/td/span/span[3]')))
        click_element.click()
        print("This is page: {n}")

# Optionally, close the driver if no further actions are required
# driver.quit()
