from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5)

def login():
    OAG_login_url = "https://analytics.oag.com/analyser-client/home"
    driver.get(OAG_login_url)
    username = "missbach@mcc-berlin.net"
    password = "OAG#MCC#2023"
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(password + Keys.ENTER)


def navigate_to_job_bin():
    traffic_analyser_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Traffic Analyser")))
    traffic_analyser_link.click()
    my_oag = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div/nav/ul/li[2]/a')))
    my_oag.click()
    job_bin =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div/nav/ul/li[2]/ul/li[3]/a')))
    job_bin.click()
    time.sleep(4)

def select_50_reports():
    select = driver.find_element(By.XPATH, '//*[@id="pageSizeOptions"]/option[3]')
    select.click()

def delete():
    while True:
        try:
            # Try to click the delete button

            time.sleep(2)
            
            delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@type="button"][contains(@class,"table__cell_delete")]')))
            delete_button.click()
            
            # Wait for the modal to appear by a more reliable indicator, such as a visible text or class that's less likely to change.
            modal = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "ui-dialog")]//button[contains(text(), "Yes")]')))
            
            # Confirm deletion by clicking the 'Yes' button
            confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "ui-dialog")]//button[contains(text(), "Yes")]')))
            confirm_button.click()

            # Wait a bit for the page to update after deletion
            time.sleep(2)

        except TimeoutException:
            # Break the loop if no more delete buttons are found
            print("No more reports to delete or page did not respond in time.")
            break


def main():
    login()  # Initial login
    navigate_to_job_bin()
    select_50_reports()
    delete()  # Download reports
   


if __name__ == "__main__":
    main()
