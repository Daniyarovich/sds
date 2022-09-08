import pygsheets
import numpy as np
import requests
import math
import time
 
import sys 
 

gc = pygsheets.authorize(client_secret='token.json')
sh = gc.open('Binance 2.0')
wks1 = sh.worksheet_by_title("UAH - SELL")
def newmain():
    a= []
    b= []
    c= []
    d= []
    e= []
    f= []
    g= []
    # update the sheet with array
    matrix = [] 
    stry = ""
    # share the sheet with your friend
    print()
    def insertvalue(asset, amount, tradetype, bank, row, sde):
        e = ''
        try:

            headers = {
            "Accept": "*/*",

            "content-type": "application/json",
            "Host": "p2p.binance.com",
            "Origin": "https://p2p.binance.com"
            }
            data = {
            "page": 1,
            "rows":1,
            "asset":asset,
            "tradeType":tradetype,
            "fiat":"UAH",
            "payTypes":[bank],
            "transAmount":amount
            }
            r = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data)
            sp = r.text
            allinfo = sp.split('"price"');
            someinfo = allinfo[1].split('"');
            line = someinfo[1].replace('.', ',')
            
            sde.append(line)
                 
        except:
            sde.append("Пусто")

    def SELLUAH():
        insertvalue('USDT',0,'SELL','PrivatBank', "B8",a)
       
        insertvalue('BTC',0,'SELL','PrivatBank', "C8",a)
       
        insertvalue('BUSD',0,'SELL','PrivatBank', "D8",a)
        
        insertvalue('BNB',0,'SELL','PrivatBank', "E8",a)
        insertvalue('ETH',0,'SELL','PrivatBank', "F8",a)
        insertvalue('UAH',0,'SELL','PrivatBank', "G8",a)
        insertvalue('SHIB',0,'SELL','PrivatBank', "H8",a)
        matrix.append(a)
        
        
        insertvalue('USDT',0,'SELL','Monobank', "B9",b)
        insertvalue('BTC',0,'SELL','Monobank', "C9",b)
        insertvalue('BUSD',0,'SELL','Monobank', "D9",b)
        insertvalue('BNB',0,'SELL','Monobank', "E9",b)
        insertvalue('ETH',0,'SELL','Monobank', "F9",b)
        insertvalue('UAH',0,'SELL','Monobank', "G9",b)
        insertvalue('SHIB',0,'SELL','Monobank', "H9",b)
        matrix.append(b)
         
        
        insertvalue('USDT',0,'SELL','UAHfiatbalance', "B10",c)
        insertvalue('BTC',0,'SELL','UAHfiatbalance', "C10",c)
        insertvalue('BUSD',0,'SELL','UAHfiatbalance', "D10",c)
        insertvalue('BNB',0,'SELL','UAHfiatbalance', "E10",c)
        insertvalue('ETH',0,'SELL','UAHfiatbalance', "F10",c)
        insertvalue('UAH',0,'SELL','UAHfiatbalance', "G10",c)
        insertvalue('SHIB',0,'SELL','UAHfiatbalance', "H10",c)
        matrix.append(c)
        insertvalue('USDT',0,'SELL','ABank', "B11",d)
        insertvalue('BTC',0,'SELL','ABank', "C11",d)
        insertvalue('BUSD',0,'SELL','ABank', "D11",d)
        insertvalue('BNB',0,'SELL','ABank', "E11",d)
        insertvalue('ETH',0,'SELL','ABank', "F11",d)
        insertvalue('UAH',0,'SELL','ABank', "G11",d)
        insertvalue('SHIB',0,'SELL','ABank', "H11",d)
        matrix.append(d)
        insertvalue('USDT',0,'SELL','Pumbbank', "B12",e)
        insertvalue('BTC',0,'SELL','Pumbbank', "C12",e)
        insertvalue('BUSD',0,'SELL','Pumbbank', "D12",e)
        insertvalue('BNB',0,'SELL','Pumbbank', "E12",e)
        insertvalue('ETH',0,'SELL','Pumbbank', "F12",e)
        insertvalue('UAH',0,'SELL','Pumbbank', "G12",e)
        insertvalue('SHIB',0,'SELL','Pumbbank', "H12",e)
        matrix.append(e)
        
        insertvalue('USDT',0,'SELL','Sportbank', "B13",f)
        insertvalue('BTC',0,'SELL','Sportbank', "C13",f)
        insertvalue('BUSD',0,'SELL','Sportbank', "D13",f)
        insertvalue('BNB',0,'SELL','Sportbank', "E13",f)
        insertvalue('ETH',0,'SELL','Sportbank', "F13",f)
        insertvalue('UAH',0,'SELL','Sportbank', "G13",f)
        insertvalue('SHIB',0,'SELL','Sportbank', "H13",f)
        matrix.append(f)
        
        
        insertvalue('USDT',0,'SELL','Izibank', "B14",g)
        insertvalue('BTC',0,'SELL','Izibank', "C14",g)
        insertvalue('BUSD',0,'SELL','Izibank', "D14",g)
        insertvalue('BNB',0,'SELL','Izibank', "E14",g)
        insertvalue('ETH',0,'SELL','Izibank', "F14",g)
        insertvalue('UAH',0,'SELL','Izibank', "G14",g)
        insertvalue('SHIB',0,'SELL','Izibank', "H14",g)
        matrix.append(g)
        wks1.update_values('B8:H14', matrix ) 
        
        


         


    SELLUAH()
while True:
    newmain()
    time.sleep(200)
    pass




