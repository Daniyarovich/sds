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
        insertvalue('USDT',200000,'SELL','PrivatBank', "B1086",a)
       
        insertvalue('BTC',200000,'SELL','PrivatBank', "C1086",a)
       
        insertvalue('BUSD',200000,'SELL','PrivatBank', "D1086",a)
        
        insertvalue('BNB',200000,'SELL','PrivatBank', "E1086",a)
        insertvalue('ETH',200000,'SELL','PrivatBank', "F1086",a)
        insertvalue('UAH',200000,'SELL','PrivatBank', "G1086",a)
        insertvalue('SHIB',200000,'SELL','PrivatBank', "H1086",a)
        matrix.append(a)
        
        
        insertvalue('USDT',200000,'SELL','Monobank', "B1087",b)
        insertvalue('BTC',200000,'SELL','Monobank', "C1087",b)
        insertvalue('BUSD',200000,'SELL','Monobank', "D1087",b)
        insertvalue('BNB',200000,'SELL','Monobank', "E1087",b)
        insertvalue('ETH',200000,'SELL','Monobank', "F1087",b)
        insertvalue('UAH',200000,'SELL','Monobank', "G1087",b)
        insertvalue('SHIB',200000,'SELL','Monobank', "H1087",b)
        matrix.append(b)
         
        
        insertvalue('USDT',200000,'SELL','UAHfiatbalance', "B108",c)
        insertvalue('BTC',200000,'SELL','UAHfiatbalance', "C108",c)
        insertvalue('BUSD',200000,'SELL','UAHfiatbalance', "D108",c)
        insertvalue('BNB',200000,'SELL','UAHfiatbalance', "E108",c)
        insertvalue('ETH',200000,'SELL','UAHfiatbalance', "F108",c)
        insertvalue('UAH',200000,'SELL','UAHfiatbalance', "G108",c)
        insertvalue('SHIB',200000,'SELL','UAHfiatbalance', "H108",c)
        matrix.append(c)
        insertvalue('USDT',200000,'SELL','ABank', "B109",d)
        insertvalue('BTC',200000,'SELL','ABank', "C109",d)
        insertvalue('BUSD',200000,'SELL','ABank', "D109",d)
        insertvalue('BNB',200000,'SELL','ABank', "E109",d)
        insertvalue('ETH',200000,'SELL','ABank', "F109",d)
        insertvalue('UAH',200000,'SELL','ABank', "G109",d)
        insertvalue('SHIB',200000,'SELL','ABank', "H109",d)
        matrix.append(d)
        insertvalue('USDT',200000,'SELL','Pumbbank', "B110",e)
        insertvalue('BTC',200000,'SELL','Pumbbank', "C110",e)
        insertvalue('BUSD',200000,'SELL','Pumbbank', "D110",e)
        insertvalue('BNB',200000,'SELL','Pumbbank', "E110",e)
        insertvalue('ETH',200000,'SELL','Pumbbank', "F110",e)
        insertvalue('UAH',200000,'SELL','Pumbbank', "G110",e)
        insertvalue('SHIB',200000,'SELL','Pumbbank', "H110",e)
        matrix.append(e)
        
        insertvalue('USDT',200000,'SELL','Sportbank', "B111",f)
        insertvalue('BTC',200000,'SELL','Sportbank', "C111",f)
        insertvalue('BUSD',200000,'SELL','Sportbank', "D111",f)
        insertvalue('BNB',200000,'SELL','Sportbank', "E111",f)
        insertvalue('ETH',200000,'SELL','Sportbank', "F111",f)
        insertvalue('UAH',200000,'SELL','Sportbank', "G111",f)
        insertvalue('SHIB',200000,'SELL','Sportbank', "H111",f)
        matrix.append(f)
        
        
        insertvalue('USDT',200000,'SELL','Izibank', "B112",g)
        insertvalue('BTC',200000,'SELL','Izibank', "C112",g)
        insertvalue('BUSD',200000,'SELL','Izibank', "D112",g)
        insertvalue('BNB',200000,'SELL','Izibank', "E112",g)
        insertvalue('ETH',200000,'SELL','Izibank', "F112",g)
        insertvalue('UAH',200000,'SELL','Izibank', "G112",g)
        insertvalue('SHIB',200000,'SELL','Izibank', "H112",g)
        matrix.append(g)
        wks1.update_values('B106:H112', matrix ) 
        
        


         


    SELLUAH()



while True:
    newmain()
    time.sleep(200)
    pass