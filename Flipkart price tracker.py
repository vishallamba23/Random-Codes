#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup as bs
import ctypes
import time
import random




#Current price of the laptop
price = '₹1,19,990'

print('Welcome to Flipkart Laptop Price Tracker! The current price is ' + price + '.\n\n')

#url = 'https://www.flipkart.com/acer-predator-helios-300-core-i7-8th-gen-8-gb-16-optane-2-tb-hdd-windows           -10-home-6-graphics-ph315-51-785w-gaming-laptop/p/itmfhbwsnh7e2jfv?pid=COMFHBWSBADFEREG&srno=s_1_2           &otracker=AS_Query_HistoryAutoSuggest_0_13&otracker1=AS_Query_HistoryAutoSuggest_0_13&lid=LSTCOMFHBW           SBADFEREGGMBPB0&fm=SEARCH&iid=93cf2bf6-daaa-4861-82f6-d339ff6ac1b3.COMFHBWSBADFEREG.SEARCH&ppt=sp&ppn           =sp&ssid=qhd61vl4eo0000001562252105899&qH=4aa32b2ea749cb27'
    
    #Get the current listed price using html data of page
#response = requests.get(url)     
#soup = bs(response.content, 'html.parser')

#Check infinitely for price update


while True:

    #URL of item listing on flipkart
 #   url = 'https://www.flipkart.com/acer-predator-helios-300-core-i7-8th-gen-8-gb-16-optane-2-tb-hdd-windows           -10-home-6-graphics-ph315-51-785w-gaming-laptop/p/itmfhbwsnh7e2jfv?pid=COMFHBWSBADFEREG&srno=s_1_2           &otracker=AS_Query_HistoryAutoSuggest_0_13&otracker1=AS_Query_HistoryAutoSuggest_0_13&lid=LSTCOMFHBW           SBADFEREGGMBPB0&fm=SEARCH&iid=93cf2bf6-daaa-4861-82f6-d339ff6ac1b3.COMFHBWSBADFEREG.SEARCH&ppt=sp&ppn           =sp&ssid=qhd61vl4eo0000001562252105899&qH=4aa32b2ea749cb27'
    url = 'http://bit.ly/30AlmaX'   
    #Get the current listed price using html data of page
    response = requests.get(url)     
    soup = bs(response.content, 'html.parser')

    stock = soup.find('div', class_ = '_9-sL7L')

    if (stock is not None) and (stock.get_text() == 'Sold Out'):
        rand = random.randint(1,18) * 200
        print('Laptop is currently sold out. Next check for availability in {} minutes.'.format(int(rand / 60)))
        time.sleep(rand)

    else:
        print('\nLaptop is now in stock!!\n')
        ctypes.windll.user32.MessageBoxW(0, 'Hurray!!', "The laptop is now in stock!", 1)

        while stock is None:

            data = soup.find("div", {"class":"_1vC4OE _3qQ9m1"})


            #if price unchcnged, check again after 30 minutes
            if data.get_text() == price:


                rand = random.randint(1,18) * 200
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                print('Performing price check at ' + str(current_time) + '.')
                print('Price is unchanged. Next check in {} minutes.\n'.format(int(rand / 60)))
                time.sleep(rand)
                stock = soup.find('div', class_ = '_9-sL7L')
                
            #if price changed, show a dialog box notification with the updated price and repeat
            else:
                
                new_price = data.get_text()
                rand = random.randint(1,18) * 200
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                print('Performing price check at ' + str(current_time) + '.')
                print('ALert! The price has changed. The updated price is ' + new_price)
                print('Next check in {} minutes.\n'.format(int(rand / 60)))
                
                ctypes.windll.user32.MessageBoxW(0, 'New price = ' + new_price, "The price has changed!", 1)
                price = new_price
                time.sleep(rand)
                stock = soup.find('div', class_ = '_9-sL7L')
                if stock is not None:
                    t = time.localtime()
                    current_time = time.strftime("%H:%M:%S", t)
                    print('Laptop is now out of stock :( (Current time is' +  str(current_time) + '.')
                    ctypes.windll.user32.MessageBoxW(0, 'Out of stock', "The laptop is out of stock!", 1)



        
























