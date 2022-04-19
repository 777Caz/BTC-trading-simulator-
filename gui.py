import tkinter
from tkinter import *
import numpy as np
import pandas as pd
#Data Source
import yfinance as yf




stock = yf.Ticker("BTC-USD") 

#the downloaded data has different parts, selects only the needed information
C_price = stock.info['regularMarketPrice'] 

# prints the current price of Bitcoin as a float
print("Current Price of Bitcoin: $", C_price)

#gets current market price as an integer

#opens the txt file and splits the lines
b = open('t.txt', "r").read().splitlines()

#creates and empty array
balance = []

#intitates loop
for b in b:
	#adds every value that its seperated to the array
	balance.append(b.split(" - "))
 #loop endds when there are no more values 

#prints the balance details array
print(balance)

def ResetAccount():
    b = open('t.txt', "r").read().splitlines()
    balance = []
    for b in b:
            balance.append(b.split(" - "))
    new_port = [100000, 0, 0, 0, 0, 0, 0, 0]
    new_b = open('t.txt', 'w')
    new_b.write("{} - {} - {} - {} - {} - {} - {} - {}".format(new_port[0],new_port[1], new_port[2], new_port[3], new_port[4], new_port[5], new_port[6], new_port[7]))

def VeiwAccountSubroutine():
    b = open('t.txt', "r").read().splitlines()
    balance = []
    for b in b:
            balance.append(b.split(" - "))
    

    stock = yf.Ticker("BTC-USD")
    C_price = stock.info['regularMarketPrice']
    print(balance)

    profit = float(balance[0][0]) + (float(balance[0][7]) * C_price) - 100000
    per_profit = (profit/100000)*100
    print("%", per_profit)
    new_port = [0, 0, 0, 0, 0, 0, 0, 0]
    new_port[0] = balance[0][0] #current balance
    new_port[1] = balance[0][1] #long or short
    new_port[2] = balance[0][2] # total money in
    new_port[3] = profit #profti loss
    new_port[4] = per_profit # profit loss %
    new_port[5] = balance[0][5] # shows the price bought at
    new_port[6] = C_price
    new_port[7] = float(balance[0][7])

    summy = """
Portfolio:
Cash:...........$""", new_port[0], """
number of trades:""", new_port[1], """
Current Price:..$""", C_price, """
Money invested:.$""", new_port[2], """
Profit:.........$""", profit, """,""", per_profit,"""%
Quantity of Bitcoin in account: """, balance[0][7], """BTC
"""
    summay = Label(main, text = summy, padx = 90, pady = 40)
    summay.place(x=600, y=650)

    new_b = open('t.txt', 'w')
    new_b.write("{} - {} - {} - {} - {} - {} - {} - {}".format(new_port[0],new_port[1], new_port[2], new_port[3], new_port[4], new_port[5], new_port[6], new_port[7]))

def SellSubroutine():
    b = open('t.txt', "r").read().splitlines()
    balance = []
    for b in b:
            balance.append(b.split(" - "))
    sell = float(value)
    new_port = [0, 0 ,0 ,0 ,0, 0 ,0, 0]
    
    if sell > float(balance[0][7]):
        print("Not enough bitcoins to sell, please enter a lower amount:")

    else:
        stock = yf.Ticker("BTC-USD")
        C_price = stock.info['regularMarketPrice']
        profit = (float(balance[0][7]) * C_price) - (float(balance[0][7]) * float(balance[0][6]))
        per_profit = (profit/ float(balance[0][2]))*100
        new_port[0] = float(balance[0][0]) + (sell * C_price)
        new_port[1] = int(balance[0][1])
        new_port[2] = float(balance[0][2]) - (sell * C_price)
        new_port[3] = profit
        new_port[4] = per_profit
        new_port[5] = balance[0][5]
        new_port[6] = C_price
        new_port[7] = sell - float(balance[0][7])
        summy = """
You have sold""", sell, "Bitcoins for a total price of $" , sell*C_price, """at $""", C_price, """each
Trade summary:
Total Cash balance: $""", new_port[0], """
Profit from this trade: $""", (sell*C_price - float(balance[0][6])), """
Total account profit: $""", profit, """
Total account % change: """, per_profit, """%
Total amount of trades: """, new_port[1], """
Quantity of Bitcoin remaining: """, new_port[7], """BTC"""
        new_b = open('t.txt', 'w')
        new_b.write("{} - {} - {} - {} - {} - {} - {} - {}".format(new_port[0],new_port[1], new_port[2], new_port[3], new_port[4], new_port[5], new_port[6], new_port[7]))
        summay = Label(main, text = summy, padx = 90, pady = 40)
        summay.place(x=10, y=650)

def quitCommand():
    main.destroy()

def BuySubroutine():
    b = open('t.txt', "r").read().splitlines()
    balance = []
    for b in b:
            balance.append(b.split(" - "))
    q = float(value)
    stock = yf.Ticker("BTC-USD")
    C_price = stock.info['regularMarketPrice']

    t_margin = q*C_price
    new_port = [0, 0 ,0 ,0 ,0, 0 ,0, 0]

    liqud_money = (float(balance[0][0])-t_margin)
    profit_loss = (C_price * q) - t_margin
    change = (((t_margin/q) - C_price)/(t_margin/q))*100
    price_bought = C_price

    new_port[0] = liqud_money
    new_port[1] = int(balance[0][1]) + 1 #number of trades
    new_port[2] = t_margin # how much money is in 
    new_port[3] = profit_loss #the current price - price bought at
    new_port[4] = change # % profit but in perentage
    new_port[5] = C_price #holds the current value of the asset bought
    new_port[6] = price_bought #makes a memory for what the asset was bought a
    new_port[7] = q + float(balance[0][7])
    print(new_port)
	
    new_b = open('t.txt', 'w')
    new_b.write("{} - {} - {} - {} - {} - {} - {} - {}".format(new_port[0],new_port[1], new_port[2], new_port[3], new_port[4], new_port[5], new_port[6], new_port[7]))

    summy = """
    Order summary - 
    Average price: $""", C_price, """
    Total margin: $""", t_margin, """
    Spare funds: $""", liqud_money, """
    Profit / Loss: $""", profit_loss, """
    % Change: """, change, """%
    Quantity of Bitcoin in account: """, new_port[7] 
    
    summay = Label(main, text = summy, padx = 240, pady = 40)
    summay.place(x=10, y=650)



main = tkinter.Tk()
main.geometry('1660x900')
main.configure(bg='black')
main.title('Bitcoin simulator')
amount = float(0)

Quantity = Label(main, text='Quantity: ' + str(amount),bg='white',fg='black',font=('comic sans',18,'bold'))
QuantityEntry = Entry(main,bg='white',font=('comic sans',18,'bold'))
def quantityConfirm():
    global value
    value = QuantityEntry.get()
    amount = value
    print(amount)
    Quantity = Label(main, text='Quantity: ' + str(amount),bg='white',fg='black',font=('comic sans',18,'bold'))

    Quantity.place_forget()
    Quantity = Label(main, text='Quantity: ' + str(amount),bg='white',fg='black',font=('comic sans',18,'bold'))
    Quantity.place(x=1300,y=160)

ConfirmQuantity = Button(main,text='confirm quantity',fg='Black',font=('comic sans',20,'bold'),padx=15,pady=15,command=quantityConfirm)


Title = Label(main, text='Bitcoin Trading Simulator',bg='white',fg='black',font=('comic sans',35,'bold'))

#Buy and sell options
BuyButton = Button(main, text='Buy',bg='green',fg='black',font=('comic sans',18,'bold'),command=BuySubroutine,padx=15,pady=15)
SellButton = Button(main, text='Sell',bg='red',fg='black',font=('comic sans',18,'bold'),command=SellSubroutine,padx=15,pady=15)
ViewAccountButton = Button(main, text = 'Veiw Account \n Balance', bg= 'purple', fg = 'white', font=('comic sans', 18, 'bold'), command = VeiwAccountSubroutine, padx=15, pady=15)
ResetAccountButton = Button(main, text = 'Reset Account', bg= 'orange', fg = 'black', font=('comic sans', 18, 'bold'), command = ResetAccount, padx=15, pady=15)
#quit option
QuitButton = Button(main,text='Quit',bg='red',fg='black',font=('comic sans',18,'bold'),command=quitCommand,padx=15,pady=15)

trading_balance = Label(main, text='Bitcoin trading simulator',bg='white',fg='black',font=('comic sans',35,'bold'))

from PIL import Image,ImageTk
mainPosterImage = ImageTk.PhotoImage(Image.open('BTCUSD.png'))

posterLabel = tkinter.Label(image=mainPosterImage, width= 700, height= 400)

Title.place(x=300,y=50)
Quantity.place(x=1300,y=160)
BuyButton.place(x=1250,y=400)
SellButton.place(x=1430,y=400)
QuitButton.place(x=1560,y=0)
QuantityEntry.place(x=1250,y=240)
ConfirmQuantity.place(x=1250,y=290)
ViewAccountButton.place(x=1380,y=760)
ResetAccountButton.place(x=1150, y=760)
posterLabel.place(x=100, y=160)

#bitcoin grpah
import mplfinance as mpf
import requests
def crypto_candles (start_time, base_currency, vs_currency, interval):
    url = f'https://dev-api.shrimpy.io/v1/exchanges/binance/candles'
    payload = {'interval': interval, 'baseTradingSymbol': base_currency, 
               'quoteTradingSymbol': vs_currency, 'startTime': start_time}
    response = requests.get(url, params=payload)
    data = response.json()
    open_p, close_p, high_p, low_p, time_p = [], [], [], [], []
    for candle in data:
         open_p.append(float(candle ['open']))
         high_p.append(float(candle ['high']))
         low_p.append(float(candle ['low']))
         close_p.append(float(candle ['close']))
         time_p.append(1)

    raw_data = {
         'Date': pd.DatetimeIndex (time_p),
         'Open': open_p,
         'High': high_p,
         'Low': low_p,
         'Close': close_p}
    df = pd.DataFrame (raw_data).set_index('Date')
    print (df)
    mpf.plot(df, type='candle', style='charles', title=base_currency, ylabel='EUR')
    mpf.show()
    return df
crypto_candles (start_time='2020-10-09', base_currency='BTC', vs_currency='EUR', interval='1d')

#crypto_candles (start_time='2021-04-09', base_currency='BTC', vs currency='EUR', interval='1h')

main.mainloop()

