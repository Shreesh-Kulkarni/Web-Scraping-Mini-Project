import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *
from tkinter import ttk

# Initialize the driver
driver = webdriver.Chrome()

# Create the Excel workbook
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = 'Scraped Data'
sheet.append(['Title', 'Price'])

# Create the GUI
root = Tk()
root.title('Scrape Data')
root.geometry('400x300')

# Create the label
label = Label(root, text='Enter a search term:')
label.pack()

# Create the entry field
search_term = StringVar()
entry = Entry(root, textvariable=search_term)
entry.pack()

# Create the button
def scrape_data():
    # Get the search term
    term = search_term.get()

    # Navigate to the website
    driver.get(f'https://www.amazon.com/s?k={term}')

    # Wait for the page to load
    time.sleep(5)

    # Scrape the data
    results = driver.find_elements(By.CSS_SELECTOR, '.s-result-item')

    for result in results:
        try:
            title = result.find_element(By.CSS_SELECTOR, 'h2').text
            price = result.find_element(By.CSS_SELECTOR, '.a-price-whole').text
            sheet.append([title, price])
        except:
            pass

    # Save the Excel workbook
    workbook.save(f'{term}.xlsx')

# Create the button
button = Button(root, text='Scrape Data', command=scrape_data)
button.pack()

# Start the GUI
root.mainloop()
