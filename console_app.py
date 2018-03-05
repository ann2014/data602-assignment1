# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file for a console_based trading application.
"""

from prettytable import PrettyTable
import urllib.request as req
import re
   
menu = ['Buy', 'Sell', 'Show Blotter', 'Show P/L', 'Quit' ]
equities = ('GOOG', 'AAPL', 'GE', 'DDD', 'TNET')
blotter = PrettyTable()
blotter.field_names = ['Side', 'Volume', 'Symbol', 'Market Price', 'Cash Change']

pl = PrettyTable()
pl.field_names = ['Side', 'Position or Inventory', 'UPL', 'RPL', 'WAP']

### FUNCTIONS ### 
# Menu Bar
def display_menu(menu):
    for m in menu:
        print(str(menu.index(m) + 1) + " - " + m)
    print('Choose an option:')

    
def valid_selection(x):
        try:
            return True 
        except ValueError:
            return print('Please select 1 - 5 only.')


simulate = True
def get_quote(symbol, simulate = False):
    #https://stackoverflow.com/questions/46080427/webscraping-in-python
    url = "https://finance.yahoo.com/quote/" + symbol + "?p=" + symbol
    htmlfile = req.urlopen(url)
    htmltext = htmlfile.read()
    #open('temp.htm', 'w').write(str(htmltext))
    #exp = '<span class="Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)" data-reactid="14"><!-- react-text: 15 -->154.49<!'
    #exp.find('  ')
    #re.sub(r'[().]', lambda m: '\\'+m.group(), exp)
    regex = '<span class="Trsdu\\(0\\.3s\\) Trsdu\\(0\\.3s\\) Fw\\(b\\) Fz\\(36px\\) Mb\\(-4px\\) D\\(b\\)" data-reactid="14"><!-- react-text: 15 -->([^<]+)<'
    price_text = re.findall(regex, str(htmltext))[0]
    price = float(price_text.replace(",", ""))
    #print (price)
    return price

### MAIN PROGRAM ###
pl.add_row(['GOOG', 0, 0, 0, 0])
pl.add_row(['AAPL', 0, 0, 0, 0])
pl.add_row(['GE', 0, 0, 0, 0])
pl.add_row(['DDD', 0, 0, 0, 0])
pl.add_row(['TNET', 0, 0, 0, 0])
pl.add_row(['Cash', 100000, 0, 0, 0])

done = False
while not done:
    display_menu(menu)
    selected = int(input())
    valid_selection(selected)

    if selected == 1 or selected == 2:
        display_menu(equities)
        equity_selected = int(input("Please select a number: "))
        valid_selection(equity_selected)
        equity_volume = int(input("Please enter a volume for the equity: "))
        price = float(get_quote(equities[equity_selected - 1]))
        if selected == 1:
            sign = - 1
        else:
            sign = 1
        cash = price * equity_volume * sign
        #wap = sum(blotter[5:5])/sum(blotter['Volume'])
        blotter.add_row([menu[selected-1], equity_volume, equities[equity_selected - 1], price, cash])
    elif selected == 3 or selected == 4:
        if(selected == 3):
            print(blotter)
        else:
            print(pl)
    elif selected == 5:
        done = True
        print('You selected to exit the trading system. Good Bye!')
    else:
        print("\nYou entered an invalid selection, please enter a number 1 - 5:\n")
        
