import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
from cryptoscrape import scrape_data
import tkinter as tk
from tkinter import filedialog

def export_to_excel():
    # Get input value for c from the user
    c = int(input_entry.get())
    # Scrape data from CoinMarketCap
    df = scrape_data(c)
    # Get filename to save Excel file
    filename = filedialog.asksaveasfilename(defaultextension='.xlsx')
    # Export data to Excel file
    df.to_excel(filename, index=False)

# Create main window
root = tk.Tk()
root.title("CoinMarketCap Scraper")

# Create input label and entry
input_label = tk.Label(root, text="Enter value for no of coins to be scraped:")
input_label.pack()
input_entry = tk.Entry(root)
input_entry.pack()

# Create export button
export_button = tk.Button(root, text="Export to Excel", command=export_to_excel)
export_button.pack()

# Start main loop
root.mainloop()