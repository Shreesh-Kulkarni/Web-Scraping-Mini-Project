import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
from cryptoscrape import scrape_data
from PIL import Image, ImageTk

def export_to_excel():
    # Get input value for c from the user
    c = int(input_entry.get())
    if c > 100 or c<=0:
        messagebox.showerror("Error", "Value for no of coins should be a natural number not more than 100")
        return
    # Scrape data from CoinMarketCap
    df = scrape_data(c)
    # Get filename to save Excel file
    filename = filedialog.asksaveasfilename(defaultextension='.xlsx')
    # Export data to Excel file
    df.to_excel(filename, index=False)

# Create main window
root = tk.Tk()
root.title("CoinMarketCap Scraper")

# Set window size and full-screen mode
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width, height))
root.attributes("-fullscreen", True)

# Load background image
bg_image = Image.open("cryptocurrency_background.jpg")
bg_image = bg_image.resize((width, height), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create background label
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0)

# Load cryptocurrency icons
btc_icon = Image.open("bitcoin_icon.jpg")
btc_icon = btc_icon.resize((50, 50), Image.ANTIALIAS)
btc_photo = ImageTk.PhotoImage(btc_icon)

eth_icon = Image.open("ethereum_icon.png")
eth_icon = eth_icon.resize((50, 50), Image.ANTIALIAS)
eth_photo = ImageTk.PhotoImage(eth_icon)

ltc_icon = Image.open("litecoin_icon.png")
ltc_icon = ltc_icon.resize((50, 50), Image.ANTIALIAS)
ltc_photo = ImageTk.PhotoImage(ltc_icon)

# Create icon labels
btc_label = tk.Label(root, image=btc_photo)
btc_label.place(x=50, y=30)

eth_label = tk.Label(root, image=eth_photo)
eth_label.place(x=150, y=30)

ltc_label = tk.Label(root, image=ltc_photo)
ltc_label.place(x=250, y=30)

# Create input label and entry
input_label = tk.Label(root, text="Enter value for no of coins to be scraped:", font=("HP Simplified", 20), bg="#d6d6d6")
input_label.place(x=(width-400)/2, y=height/2-50)

input_entry = tk.Entry(root, font=("Verdana", 16), bg="#d6d6d6")
input_entry.place(x=(width-400)/2, y=height/2, width=400)

# Create export button
export_button = tk.Button(root, text="Export to Excel", font=("Arial", 16), bg="#81c784", fg="white", command=export_to_excel)
export_button.place(x=(width-200)/2, y=height/2+60, width=200, height=50)

# Start main loop
root.mainloop()
