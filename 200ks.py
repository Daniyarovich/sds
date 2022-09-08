import pygsheets
import numpy as np
import requests
import math
import sys 
import time
gc = pygsheets.authorize(client_secret='token1.json')
sh = gc.open('Binance 2.0')
wks1 = sh.worksheet_by_title("UAH - BUY")
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

    def BUYUAH():
        insertvalue('USDT',200000,'BUY','PrivatBank', "B1086",a)
       
        insertvalue('BTC',200000,'BUY','PrivatBank', "C1086",a)
       
        insertvalue('BUSD',200000,'BUY','PrivatBank', "D1086",a)
        
        insertvalue('BNB',200000,'BUY','PrivatBank', "E1086",a)
        insertvalue('ETH',200000,'BUY','PrivatBank', "F1086",a)
        insertvalue('UAH',200000,'BUY','PrivatBank', "G1086",a)
        insertvalue('SHIB',200000,'BUY','PrivatBank', "H1086",a)
        matrix.append(a)
        
        
        insertvalue('USDT',200000,'BUY','Monobank', "B1087",b)
        insertvalue('BTC',200000,'BUY','Monobank', "C1087",b)
        insertvalue('BUSD',200000,'BUY','Monobank', "D1087",b)
        insertvalue('BNB',200000,'BUY','Monobank', "E1087",b)
        insertvalue('ETH',200000,'BUY','Monobank', "F1087",b)
        insertvalue('UAH',200000,'BUY','Monobank', "G1087",b)
        insertvalue('SHIB',200000,'BUY','Monobank', "H1087",b)
        matrix.append(b)
         
        
        insertvalue('USDT',200000,'BUY','UAHfiatbalance', "B108",c)
        insertvalue('BTC',200000,'BUY','UAHfiatbalance', "C108",c)
        insertvalue('BUSD',200000,'BUY','UAHfiatbalance', "D108",c)
        insertvalue('BNB',200000,'BUY','UAHfiatbalance', "E108",c)
        insertvalue('ETH',200000,'BUY','UAHfiatbalance', "F108",c)
        insertvalue('UAH',200000,'BUY','UAHfiatbalance', "G108",c)
        insertvalue('SHIB',200000,'BUY','UAHfiatbalance', "H108",c)
        matrix.append(c)
        insertvalue('USDT',200000,'BUY','ABank', "B109",d)
        insertvalue('BTC',200000,'BUY','ABank', "C109",d)
        insertvalue('BUSD',200000,'BUY','ABank', "D109",d)
        insertvalue('BNB',200000,'BUY','ABank', "E109",d)
        insertvalue('ETH',200000,'BUY','ABank', "F109",d)
        insertvalue('UAH',200000,'BUY','ABank', "G109",d)
        insertvalue('SHIB',200000,'BUY','ABank', "H109",d)
        matrix.append(d)
        insertvalue('USDT',200000,'BUY','Pumbbank', "B110",e)
        insertvalue('BTC',200000,'BUY','Pumbbank', "C110",e)
        insertvalue('BUSD',200000,'BUY','Pumbbank', "D110",e)
        insertvalue('BNB',200000,'BUY','Pumbbank', "E110",e)
        insertvalue('ETH',200000,'BUY','Pumbbank', "F110",e)
        insertvalue('UAH',200000,'BUY','Pumbbank', "G110",e)
        insertvalue('SHIB',200000,'BUY','Pumbbank', "H110",e)
        matrix.append(e)
        
        insertvalue('USDT',200000,'BUY','Sportbank', "B111",f)
        insertvalue('BTC',200000,'BUY','Sportbank', "C111",f)
        insertvalue('BUSD',200000,'BUY','Sportbank', "D111",f)
        insertvalue('BNB',200000,'BUY','Sportbank', "E111",f)
        insertvalue('ETH',200000,'BUY','Sportbank', "F111",f)
        insertvalue('UAH',200000,'BUY','Sportbank', "G111",f)
        insertvalue('SHIB',200000,'BUY','Sportbank', "H111",f)
        matrix.append(f)
        
        
        insertvalue('USDT',200000,'BUY','Izibank', "B112",g)
        insertvalue('BTC',200000,'BUY','Izibank', "C112",g)
        insertvalue('BUSD',200000,'BUY','Izibank', "D112",g)
        insertvalue('BNB',200000,'BUY','Izibank', "E112",g)
        insertvalue('ETH',200000,'BUY','Izibank', "F112",g)
        insertvalue('UAH',200000,'BUY','Izibank', "G112",g)
        insertvalue('SHIB',200000,'BUY','Izibank', "H112",g)
        matrix.append(g)
        wks1.update_values('B106:H112', matrix ) 
        
        


         

    BUYUAH()

while True:
    newmain()
    time.sleep(200)
    pass




