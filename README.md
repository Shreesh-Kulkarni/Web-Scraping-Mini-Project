# Web-Scraping-Mini-Project
A python tool/wrapper which scrapes dynamic data from dynamic websites and stores it. The wrapper might be configured to scrape static data as well, come the necessity.

##Steps to run the scraper:-
    1. Clone the repository and run the gui.py file. 
    2. Wait 20seconds for the webpage to load. Scrolling through the page is suggested to prevent any erratic data
    3. Pick your choice in the GUI. If excel file is selected, you are asked to find a location to download the excel file.
    4. There you go, your crypto dataset is ready.
   
   
   ##Note: The code is configured for the first 14 currencies of the website as thats the maximum elements that could fit in one frame. Selenium's docs do not mention any feasible fix for this. The only option is to manually change the no of currencies being scraped which can be done in the num array in stockscrape.py. The polling rate of this scraper is once every 20 seconds.(0.05Hz). This is the most optimal frequency for perfect sampling of data. Change it at your own risk.
   You can observe the changes by pressing the scrape data button every 20-30 seconds and record your observations.
