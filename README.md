# Web-Scraping-Mini-Project
A python tool/wrapper which scrapes dynamic data from dynamic websites and stores it. The wrapper might be configured to scrape static data as well, come the necessity.

## Steps to run the scraper:-
    1. Clone the repository and run the gui.py file.
    2. Input the size of the dataset
    3.  Wait 20seconds for the webpage to load. Scrolling through the page is suggested to prevent any erratic data
    4. you are asked to find a location to download the excel file after a few seconds.
    5. There, you go, your crypto dataset is ready.
   
   
   ## Note: The code is configured for the first 100 currencies of the website as thats the maximum elements that could fit in one webpage. If you want to scrape the next 100 currencies,simply change the webpage link to page2. Selenium's docs do not mention any feasible fix for this minor issue as dynamic data cannot be accessed from different webpages of the same parent webpage due to varying xpaths. 
