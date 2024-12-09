import yfinance as yahooFinance
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import tkinter as tk
from PIL import ImageTk, Image


def get_entry_value(master, entry):
    global value
    value = entry.get()
    value = value.upper()
    ans = image_ans(value)

    newWindow = tk.Toplevel(master)
    newWindow.title(value)
    if ans == 'BUY':
        x = tk.Label(newWindow, text=ans, font=('Arial', 20, 'bold'), fg='green')
    elif ans == 'SALE':
        x = tk.Label(newWindow, text=ans, font=('Arial', 20, 'bold'), fg='red')
    else:
        x = tk.Label(newWindow, text=ans, font=('Arial', 20, 'bold'))
    x.pack()
    img = ImageTk.PhotoImage(Image.open(r'plot.png'))
    panel = tk.Label(newWindow, image=img)
    panel.image = img
    panel.pack()


def image_ans(value,end = date.today()):
    company = yahooFinance.Ticker(value)
    start = end.replace(year = end.year - 1)
    

    #Make the data frame
    df = pd.DataFrame(company.history(start = start,end = end))
    #Calculate the bollinger bond
    df['SMA'] = df['Close'].rolling(window=20).mean()
    df['SD'] = df['Close'].rolling(window=20).std()
    df['BB_UP'] = df['SMA'] + (2 * df['SD'])
    df['BB_DOWN'] = df['SMA'] - (2 * df['SD'])
    
    #make the plot (or plot the plot)
    fig, ax = plt.subplots()
    ax.plot(df['Close'], label='Price', color='black', linewidth=3)
    ax.plot(df['SMA'], label='SMA-20', color='blue', linewidth=1)
    ax.plot(df['BB_UP'], label='BB_UP', color='green', linewidth=1)
    ax.plot(df['BB_DOWN'], label='BB_DOWN', color='red', linewidth=1)
    ax.legend()

    plt.savefig(r'plot.png')
    if df['Close'].iloc[-1] > df['BB_UP'].iloc[-1]:
        return 'SALE'
    elif df['Close'].iloc[-1] < df['BB_DOWN'].iloc[-1]:
        return 'BUY'
    else:
        return 'HOLD'


def master_win():
    # Create the Tkinter window
    master = tk.Tk()
    master.geometry('250x100')

    master.title('Stock analyzer')
    discription = tk.Label(
        master,
        text='Input ticker of a company \n and the programme will tell you if you should\nhold, buy more stock or sell it.',
    )
    discription.pack()
    # Create an Entry widget
    entry = tk.Entry(master)
    entry.pack()

    # Create a button to trigger value retrieval
    button = tk.Button(master, text='Search for Ticker')
    button.bind('<Button>', lambda e: get_entry_value(master, entry))
    button.pack()


def main():
    master_win()
    tk.mainloop()
    exit(0)


if __name__ == '__main__':
    main()
