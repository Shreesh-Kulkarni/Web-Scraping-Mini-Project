import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
from cryptoscrape import scrape_data
def create_dataframe():
    d = scrape_data()
    df = pd.DataFrame.from_dict(d, orient='index', columns=['Price', 'Market Cap', 'Volume', 'Circulating Supply'])
    return df

def export_to_excel():
    df = create_dataframe()
    filepath = filedialog.asksaveasfilename(defaultextension='.xlsx')
    df.to_excel(filepath)

def generate_dataframe():
    df = create_dataframe()
    messagebox.showinfo('DataFrame', f'{df}')

def build_gui():
    root = tk.Tk()
    root.title('CoinMarketCap Scraper')

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    scrape_button = tk.Button(button_frame, text='Scrape Data', command=generate_dataframe)
    scrape_button.pack(side='left', padx=5)

    export_button = tk.Button(button_frame, text='Export to Excel', command=export_to_excel)
    export_button.pack(side='left', padx=5)

    root.mainloop()

if __name__ == '__main__':
    build_gui()