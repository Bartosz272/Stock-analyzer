# Stock-analyzer
    #### Video Demo: https://youtu.be/5rMmKnHwA2Y
    #### Description:
    This code is a simple way to tell you if you should sell your stock, buy more or try to hold it.
    It uses bollinger bands, and if the price is above them you should sell it,
    below them buy it, and if its in the middle try to hold on to it.
      (when I traded a little bit during one of the courses on my uniwersity this method worked)
    At first when you start this code a window shows up and it asks you to put in ticker of a company you want to analyze
    they should be the same as on : finance.yahoo.com
    but they can be lower case, and if you make a mistake also nothing happends.
    After you put in the ticker you should press the button 'Search for Ticker'.
    When you press it a new window shows up, it contains what shold you do on the top,
    HOLD, SELL or BUY each shows up in different colour.
    Under this there is a graph showng the price of the stock and in bold black line,
    SME-20(Simple Moveing Average of 20 days) in the blue, the upper bollinger bond (BB_UP),
    and the lower bollinger bond in red (BB_DOWN)
    
    In order to calculate the data I used the pandas libary,
    first I retrived the data form yahoo.finanse using libary yfinance,
    then the data from today to year before are saved as data frame,
    then the SME and standard div is calcultated, and from this data I could get both bollinger bonds.
    
    Also for the testing pourpuses you can change the end day of the one year od historical data,
    this allows the tester to set the date to so you can chceck the solution in differen sources and chceck
    if the price should be above or below the bands.
    Without this the solution would change daily and propper testing would not be possible.
