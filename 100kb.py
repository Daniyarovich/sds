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
        insertvalue('USDT',100000,'SELL','PrivatBank', "B932",a)
       
        insertvalue('BTC',100000,'SELL','PrivatBank', "C932",a)
       
        insertvalue('BUSD',100000,'SELL','PrivatBank', "D932",a)
        
        insertvalue('BNB',100000,'SELL','PrivatBank', "E932",a)
        insertvalue('ETH',100000,'SELL','PrivatBank', "F932",a)
        insertvalue('UAH',100000,'SELL','PrivatBank', "G932",a)
        insertvalue('SHIB',100000,'SELL','PrivatBank', "H932",a)
        matrix.append(a)
        
        
        insertvalue('USDT',100000,'SELL','Monobank', "B93",b)
        insertvalue('BTC',100000,'SELL','Monobank', "C93",b)
        insertvalue('BUSD',100000,'SELL','Monobank', "D93",b)
        insertvalue('BNB',100000,'SELL','Monobank', "E93",b)
        insertvalue('ETH',100000,'SELL','Monobank', "F93",b)
        insertvalue('UAH',100000,'SELL','Monobank', "G93",b)
        insertvalue('SHIB',100000,'SELL','Monobank', "H93",b)
        matrix.append(b)
         
        
        insertvalue('USDT',100000,'SELL','UAHfiatbalance', "B94",c)
        insertvalue('BTC',100000,'SELL','UAHfiatbalance', "C94",c)
        insertvalue('BUSD',100000,'SELL','UAHfiatbalance', "D94",c)
        insertvalue('BNB',100000,'SELL','UAHfiatbalance', "E94",c)
        insertvalue('ETH',100000,'SELL','UAHfiatbalance', "F94",c)
        insertvalue('UAH',100000,'SELL','UAHfiatbalance', "G94",c)
        insertvalue('SHIB',100000,'SELL','UAHfiatbalance', "H94",c)
        matrix.append(c)
        insertvalue('USDT',100000,'SELL','ABank', "B95",d)
        insertvalue('BTC',100000,'SELL','ABank', "C95",d)
        insertvalue('BUSD',100000,'SELL','ABank', "D95",d)
        insertvalue('BNB',100000,'SELL','ABank', "E95",d)
        insertvalue('ETH',100000,'SELL','ABank', "F95",d)
        insertvalue('UAH',100000,'SELL','ABank', "G95",d)
        insertvalue('SHIB',100000,'SELL','ABank', "H95",d)
        matrix.append(d)
        insertvalue('USDT',100000,'SELL','Pumbbank', "B96",e)
        insertvalue('BTC',100000,'SELL','Pumbbank', "C96",e)
        insertvalue('BUSD',100000,'SELL','Pumbbank', "D96",e)
        insertvalue('BNB',100000,'SELL','Pumbbank', "E96",e)
        insertvalue('ETH',100000,'SELL','Pumbbank', "F96",e)
        insertvalue('UAH',100000,'SELL','Pumbbank', "G96",e)
        insertvalue('SHIB',100000,'SELL','Pumbbank', "H96",e)
        matrix.append(e)
        
        insertvalue('USDT',100000,'SELL','Sportbank', "B97",f)
        insertvalue('BTC',100000,'SELL','Sportbank', "C97",f)
        insertvalue('BUSD',100000,'SELL','Sportbank', "D97",f)
        insertvalue('BNB',100000,'SELL','Sportbank', "E97",f)
        insertvalue('ETH',100000,'SELL','Sportbank', "F97",f)
        insertvalue('UAH',100000,'SELL','Sportbank', "G97",f)
        insertvalue('SHIB',100000,'SELL','Sportbank', "H97",f)
        matrix.append(f)
        
        
        insertvalue('USDT',100000,'SELL','Izibank', "B98",g)
        insertvalue('BTC',100000,'SELL','Izibank', "C98",g)
        insertvalue('BUSD',100000,'SELL','Izibank', "D98",g)
        insertvalue('BNB',100000,'SELL','Izibank', "E98",g)
        insertvalue('ETH',100000,'SELL','Izibank', "F98",g)
        insertvalue('UAH',100000,'SELL','Izibank', "G98",g)
        insertvalue('SHIB',100000,'SELL','Izibank', "H98",g)
        matrix.append(g)
        wks1.update_values('B92:H98', matrix ) 
        
        


         

    SELLUAH()
while True:
    newmain()
    time.sleep(200)
    pass




