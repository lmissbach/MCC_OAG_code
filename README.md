# MCC_OAG_code
This private repo tracks the progress on scraping OAG 

### 13/03 checkpoint 
Today i worked on setting chromedriver -> Selenium needs to work with chromedriver because Selenium itself doesn't directly interact with web browsers like Google. 
Relevant for webscraping ->  chromedriver allows Selenium to interact with the parameters in the OAG homepage - avg fare destinations etc. 
It uses a driver specific to each browser to communicate and control the browser. 
chromedriver is the link between Selenium commands and Google Chrome's actions. 

Where I pick up from next time: now my Chromedriver and my google are the same version but i still get error messages in the script, next time I work on debugging 

Goal, try to run for 1 month within one country , january 2015. 
Start writing script to prompt within country flight and see how it works
How quickly can we do these prompts 
Trying code out on SkyScanner website https://www.skyscanner.de/?previousCultureSource=COOKIE&redirectedFrom=www.skyscanner.net
Using python for now 

NOTES 

Power table report -> select airport, all connections between Berlin and Paris, period you're interested in
Average fare, booking class -> Creates a table to export -> Formalt XLSX 
Problem, 1 million rows, you have to manually select combinations 
10-15 country groups, from each of them prompt the fares between groups, 220 prompts fro 6 years 


