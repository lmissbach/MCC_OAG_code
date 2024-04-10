# MCC_OAG_code
This private repo tracks the progress on scraping OAG 

# 10/04
- Must give a good think to how the big for loop will come about

### 05/04
- Automatize request such that this runs for each. Start from jan 2016
- change report export, XLSX
- report name is ORIGIN_DESTINATION_date

#### More generally on the OAG Platform 
- Understand difference between one way, two ways, aggregate
- check difference between segment and origin destination
- can it download reports together
  
#### To keep in mind for next steps 
- At some point, from module, reference, airport codes, use R or Python to remove duplicates, like in germany, aachen maastricht appears twice
- ideally in the python or smt, insert country.group -> select all countries corresponding to that-> run analysis between country groups

### 03/04
Scraping produces a report but only on the connection berlin - Munich, must make sure that it generates 
- 1) more than one connection , so not only from berlin to munich but from berlin to all the airports in the UK for example 
- 2) make sure that it can download more than one report at the time in the Job bin 
 
Also, add a commented out code in case theres the need to select a specific time frame 


### 27/03
- Working of OAG, next steps complete the code with the comments and add the segment thing to solve the error I get 
- Try to download 
- find ways to be more invisible 


### 26/03 
problem with log in detail, trying on the hertie connect page
try manually inserting the login for the password 
try to scrape the world bank data to practice ticking bozed and useful also to compare the vertical and horizontal data with other from accredited sources



### 22/03
switchd from jupyter notebook to vscode
managed scraping on a newspaper, insert things in a search bar 
https://youtu.be/NB8OceGZGjA?si=74n7tlCnRPzLqLqm this video was useful 
next time i try with skyscanner but they most likely have some protection against bots, maybe i start trying some things out on OAG but wanna be sure not to fiddle with the page too much 



### 15/03 checkpoint 
Today debugging. Problem might be that my chromedriver is not currently executable - this video is helpful https://youtu.be/Xjv1sY630Uc?si=LWF03StiQlxhz8Ty

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




