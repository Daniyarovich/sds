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
        insertvalue('USDT',20000,'SELL','PrivatBank', "B50",a)
       
        insertvalue('BTC',20000,'SELL','PrivatBank', "C50",a)
       
        insertvalue('BUSD',20000,'SELL','PrivatBank', "D50",a)
        
        insertvalue('BNB',20000,'SELL','PrivatBank', "E50",a)
        insertvalue('ETH',20000,'SELL','PrivatBank', "F50",a)
        insertvalue('UAH',20000,'SELL','PrivatBank', "G50",a)
        insertvalue('SHIB',20000,'SELL','PrivatBank', "H50",a)
        matrix.append(a)
        
        
        insertvalue('USDT',20000,'SELL','Monobank', "B51",b)
        insertvalue('BTC',20000,'SELL','Monobank', "C51",b)
        insertvalue('BUSD',20000,'SELL','Monobank', "D51",b)
        insertvalue('BNB',20000,'SELL','Monobank', "E51",b)
        insertvalue('ETH',20000,'SELL','Monobank', "F51",b)
        insertvalue('UAH',20000,'SELL','Monobank', "G51",b)
        insertvalue('SHIB',20000,'SELL','Monobank', "H51",b)
        matrix.append(b)
         
        
        insertvalue('USDT',20000,'SELL','UAHfiatbalance', "B52",c)
        insertvalue('BTC',20000,'SELL','UAHfiatbalance', "C52",c)
        insertvalue('BUSD',20000,'SELL','UAHfiatbalance', "D52",c)
        insertvalue('BNB',20000,'SELL','UAHfiatbalance', "E52",c)
        insertvalue('ETH',20000,'SELL','UAHfiatbalance', "F52",c)
        insertvalue('UAH',20000,'SELL','UAHfiatbalance', "G52",c)
        insertvalue('SHIB',20000,'SELL','UAHfiatbalance', "H52",c)
        matrix.append(c)
        insertvalue('USDT',20000,'SELL','ABank', "B53",d)
        insertvalue('BTC',20000,'SELL','ABank', "C53",d)
        insertvalue('BUSD',20000,'SELL','ABank', "D53",d)
        insertvalue('BNB',20000,'SELL','ABank', "E53",d)
        insertvalue('ETH',20000,'SELL','ABank', "F53",d)
        insertvalue('UAH',20000,'SELL','ABank', "G53",d)
        insertvalue('SHIB',20000,'SELL','ABank', "H53",d)
        matrix.append(d)
        insertvalue('USDT',20000,'SELL','Pumbbank', "B54",e)
        insertvalue('BTC',20000,'SELL','Pumbbank', "C54",e)
        insertvalue('BUSD',20000,'SELL','Pumbbank', "D54",e)
        insertvalue('BNB',20000,'SELL','Pumbbank', "E54",e)
        insertvalue('ETH',20000,'SELL','Pumbbank', "F54",e)
        insertvalue('UAH',20000,'SELL','Pumbbank', "G54",e)
        insertvalue('SHIB',20000,'SELL','Pumbbank', "H54",e)
        matrix.append(e)
        
        insertvalue('USDT',20000,'SELL','Sportbank', "B55",f)
        insertvalue('BTC',20000,'SELL','Sportbank', "C55",f)
        insertvalue('BUSD',20000,'SELL','Sportbank', "D55",f)
        insertvalue('BNB',20000,'SELL','Sportbank', "E55",f)
        insertvalue('ETH',20000,'SELL','Sportbank', "F55",f)
        insertvalue('UAH',20000,'SELL','Sportbank', "G55",f)
        insertvalue('SHIB',20000,'SELL','Sportbank', "H55",f)
        matrix.append(f)
        
        
        insertvalue('USDT',20000,'SELL','Izibank', "B56",g)
        insertvalue('BTC',20000,'SELL','Izibank', "C56",g)
        insertvalue('BUSD',20000,'SELL','Izibank', "D56",g)
        insertvalue('BNB',20000,'SELL','Izibank', "E56",g)
        insertvalue('ETH',20000,'SELL','Izibank', "F56",g)
        insertvalue('UAH',20000,'SELL','Izibank', "G56",g)
        insertvalue('SHIB',20000,'SELL','Izibank', "H56",g)
        matrix.append(g)
        wks1.update_values('B50:H56', matrix ) 
        
        


         



    SELLUAH()
    
while True:
    newmain()
    time.sleep(200)
    pass

