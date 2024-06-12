from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Check that the version of ChromeDriver is compatible with the current version of Chrome
# Sometimes updates can cause the browser to be updated to a version that is not supported by the current version of ChromeDriver

# The error you will see if that happens 
# This version of ChromeDriver only supports Chrome version 123 
# Current browser version is 125.0.6422.112 with binary path C:\Program Files\Google\Chrome\Application\chrome.exe

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 5)

# Open OAG, log in
def login():
    OAG_login_url = "https://analytics.oag.com/analyser-client/home"
    driver.get(OAG_login_url)
    username = "missbach@mcc-berlin.net"
    password = "OAG#MCC#2023"
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(username) # this inserts username in the username field
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(password + Keys.ENTER) # this inserts password and presses enter

# Selects traffic analyser and power table report
def navigate_to_power_tables():
    traffic_analyser_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Traffic Analyser"))) # this can be customized based on text 
    traffic_analyser_link.click()
    power_table_report = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Power Table Report")))
    power_table_report.click()

# Select different options for metrics
def avg_fare():
    # Select options after reaching Power Table page
    avg_fare = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Fare"))) # this can be customized based on text
    avg_fare.click()
    booking_class = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Booking Class")))
    booking_class.click()
    origin_destination = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Origin &")))
    origin_destination.click()

# Select Segment --> Inspect --> XPath --> Copy and Paste
def segment_selection():
    segment =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="radioSegment"]')))
    segment.click()

# Clicks Country-combination
# Click manually (!) the kind of combination, e.g., A-B, that is desired
def country_group(): 
    country1_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id-Y-Country-airport1_include"]')))  
    country1_checkbox.click()
    country2_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id-Y-Country-airport2_include"]')))
    country2_checkbox.click()

    tab_airport1 = wait.until(EC.element_to_be_clickable(((By.XPATH, '//*[@id="airport1-autocomplete"]/span/div[1]/div/button'))))
    tab_airport1.click()

    # group_a, group_b, group_c are the options for the group selection
    # they are customized based on what combination the code wants to scrape 
    # to use one option, simply uncomment it and comment the others
    # to comment means to put # before the line of code

    group_a = driver.find_element(By.XPATH, '//*[@id="group-options"]/div/div[3]/div[2]/div[2]/div[1]/div')
    group_a.click()

    # group_b = driver.find_element(By.XPATH, '//*[@id="group-options"]/div/div[3]/div[2]/div[2]/div[2]/div')
    # group_b.click()

    # group_c = driver.find_element(By.XPATH, '//*[@id="group-options"]/div/div[3]/div[2]/div[2]/div[3]/div')
    # group_c.click()

    ok_button = driver.find_element(By.XPATH, '//*[@id="group-options"]/div/div[4]/div[1]/input')
    ok_button.click()

    tab_airport2 = driver.find_element(By.XPATH, '//*[@id="airport2-autocomplete"]/span/div[1]/div/button') 
    tab_airport2.click()

    # same here, this is the "to" airport group selection

    # group_a = driver.find_element(By.XPATH, '//*[@id="group-options"]/div/div[3]/div[2]/div[2]/div[1]/div')
    # group_a.click()

    group_b = driver.find_element(By.XPATH, '//*[@id="group-options"]/div/div[3]/div[2]/div[2]/div[2]/div')
    group_b.click()

    # group_c = driver.find_element(By.XPATH, '//*[@id="group-options"]/div/div[3]/div[2]/div[2]/div[3]/div')
    # group_c.click()

    ok_button = driver.find_element(By.XPATH, '//*[@id="group-options"]/div/div[4]/div[1]/input')
    ok_button.click()

# Selects connection
def connection_option():
    # equals to 
    option_equal = wait.until(EC.element_to_be_clickable(((By.XPATH, '//*[@id="connections"]/div/div[1]/span/div/select/option[2]'))))
    option_equal.click()

    # 0 connections 
    option_0cons = wait.until(EC.element_to_be_clickable(((By.XPATH, '//*[@id="connections"]/div/div[2]/span/div/select/option[2]'))))
    option_0cons.click()

# Selects month - iteratively
def select_month(month_index, year):
    #Select the same month in dropdown 2 by option value
    dropdown_2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dateGroup"]/span/div[1]/div[2]/div[4]/div/span[3]/span/select')))
    dropdown_2.click()
    option_2 = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="dateGroup"]/span/div[1]/div[2]/div[4]/div/span[3]/span/select/option[{month_index}]')))
    option_2.click()

    year_index = year - 2016 + 1  # Calculation needed to select the right xpath 
    # example: 2024 - 2016 + 1 = 9
    # 9 is the position of 2024 in the xpath //*[@id="fromYear"]/option[9]

    # Select the from year
    year_dropdown_from = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fromYear"]')))
    year_dropdown_from.click()
    year_option_from = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="fromYear"]/option[{year_index}]')))
    year_option_from.click()

    # Select the same year for "to"
    year_dropdown_to = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[(@id = "toYear")]')))
    year_dropdown_to.click()
    year_option_to = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[(@id = "toYear")]/option[{year_index}]')))
    year_option_to.click()

     # Select the month in dropdown 1 by option value
    dropdown_1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dateGroup"]/span/div[1]/div[2]/div[4]/span[3]/span/select')))                                                                                                          
    dropdown_1.click()
    option_1 = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="dateGroup"]/span/div[1]/div[2]/div[4]/span[3]/span/select/option[{month_index}]')))
    option_1.click()

# Creates reports
# IMPORTANT: Change report_name for different combinations.
def export_report(month_name, year):
    report_name = f"A_B_{month_name}_{year}" # this has to be customized based on the combination of groups selected
    # report_name = f"B_A_{month_name}_{year}" 
    # report_name = f"A_A_{month_name}_{year}" 
    # report_name = f"B_B_{month_name}_{year}" 
    # report_name = f"B_C_{month_name}_{year}" 
    # report_name = f"C_B_{month_name}_{year}" 
    # report_name = f"A_C_{month_name}_{year}" 
    # report_name = f"C_A_{month_name}_{year}" 
    export_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="export-button"]/span/button')))
    export_button.click()
    report_name_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ui-id-31"]/div/div[2]/input')))
    report_name_field.send_keys(report_name + Keys.ENTER)
    finalize_export = driver.find_element(By.XPATH, '/html/body/div[46]/div[3]/div/button[1]')
    finalize_export.click()
    job_bin_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[46]/div[3]/div/button[2]')))
    job_bin_button.click()

# Execution!
def main():
    login()  # Initial login
    navigate_to_power_tables()
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    start_year = 2016
    end_year = 2024 # update the year as needed 
    start_month = 1 # January
    end_month = 12 # December
    
    for year in range(start_year, end_year + 1): # +1 because the range function is exclusive of the end value. So, if you want to include 2024, you need to add 1
        for month_index in range(start_month, end_month + 1):  # Loop from 1 to 12 for January to December
            avg_fare()
            time.sleep(2)
            segment_selection()  # Make selections 
            time.sleep(2)   
            country_group()
            time.sleep(2) 
            connection_option()
            time.sleep(2) 
            select_month(month_index, year)  # Now also pass the year
            time.sleep(2) 
            export_report(months[month_index - 1], year)  # Now also pass the year
            time.sleep(10)
            driver.get("https://analytics.oag.com/analyser-client/traffic-analyser/job-bin")
            time.sleep(60)
            driver.get("https://analytics.oag.com/analyser-client/traffic-analyser/power-tables")
            time.sleep(60) # if you dont leave it enough time to "rest" it overcharges and  it does not download all the reports, it jumps
            # this explains such long pauses between the reports, it is to avoid overcharging the server
        
if __name__ == "__main__":
    main()

driver.quit()