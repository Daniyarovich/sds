import pygsheets
import numpy as np
import requests
import math
import time
import sys  
 
 
gc = pygsheets.authorize(client_secret='token.json')
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
        insertvalue('USDT',100000,'BUY','PrivatBank', "B932",a)
       
        insertvalue('BTC',100000,'BUY','PrivatBank', "C932",a)
       
        insertvalue('BUSD',100000,'BUY','PrivatBank', "D932",a)
        
        insertvalue('BNB',100000,'BUY','PrivatBank', "E932",a)
        insertvalue('ETH',100000,'BUY','PrivatBank', "F932",a)
        insertvalue('UAH',100000,'BUY','PrivatBank', "G932",a)
        insertvalue('SHIB',100000,'BUY','PrivatBank', "H932",a)
        matrix.append(a)
        
        
        insertvalue('USDT',100000,'BUY','Monobank', "B93",b)
        insertvalue('BTC',100000,'BUY','Monobank', "C93",b)
        insertvalue('BUSD',100000,'BUY','Monobank', "D93",b)
        insertvalue('BNB',100000,'BUY','Monobank', "E93",b)
        insertvalue('ETH',100000,'BUY','Monobank', "F93",b)
        insertvalue('UAH',100000,'BUY','Monobank', "G93",b)
        insertvalue('SHIB',100000,'BUY','Monobank', "H93",b)
        matrix.append(b)
         
        
        insertvalue('USDT',100000,'BUY','UAHfiatbalance', "B94",c)
        insertvalue('BTC',100000,'BUY','UAHfiatbalance', "C94",c)
        insertvalue('BUSD',100000,'BUY','UAHfiatbalance', "D94",c)
        insertvalue('BNB',100000,'BUY','UAHfiatbalance', "E94",c)
        insertvalue('ETH',100000,'BUY','UAHfiatbalance', "F94",c)
        insertvalue('UAH',100000,'BUY','UAHfiatbalance', "G94",c)
        insertvalue('SHIB',100000,'BUY','UAHfiatbalance', "H94",c)
        matrix.append(c)
        insertvalue('USDT',100000,'BUY','ABank', "B95",d)
        insertvalue('BTC',100000,'BUY','ABank', "C95",d)
        insertvalue('BUSD',100000,'BUY','ABank', "D95",d)
        insertvalue('BNB',100000,'BUY','ABank', "E95",d)
        insertvalue('ETH',100000,'BUY','ABank', "F95",d)
        insertvalue('UAH',100000,'BUY','ABank', "G95",d)
        insertvalue('SHIB',100000,'BUY','ABank', "H95",d)
        matrix.append(d)
        insertvalue('USDT',100000,'BUY','Pumbbank', "B96",e)
        insertvalue('BTC',100000,'BUY','Pumbbank', "C96",e)
        insertvalue('BUSD',100000,'BUY','Pumbbank', "D96",e)
        insertvalue('BNB',100000,'BUY','Pumbbank', "E96",e)
        insertvalue('ETH',100000,'BUY','Pumbbank', "F96",e)
        insertvalue('UAH',100000,'BUY','Pumbbank', "G96",e)
        insertvalue('SHIB',100000,'BUY','Pumbbank', "H96",e)
        matrix.append(e)
        
        insertvalue('USDT',100000,'BUY','Sportbank', "B97",f)
        insertvalue('BTC',100000,'BUY','Sportbank', "C97",f)
        insertvalue('BUSD',100000,'BUY','Sportbank', "D97",f)
        insertvalue('BNB',100000,'BUY','Sportbank', "E97",f)
        insertvalue('ETH',100000,'BUY','Sportbank', "F97",f)
        insertvalue('UAH',100000,'BUY','Sportbank', "G97",f)
        insertvalue('SHIB',100000,'BUY','Sportbank', "H97",f)
        matrix.append(f)
        
        
        insertvalue('USDT',100000,'BUY','Izibank', "B98",g)
        insertvalue('BTC',100000,'BUY','Izibank', "C98",g)
        insertvalue('BUSD',100000,'BUY','Izibank', "D98",g)
        insertvalue('BNB',100000,'BUY','Izibank', "E98",g)
        insertvalue('ETH',100000,'BUY','Izibank', "F98",g)
        insertvalue('UAH',100000,'BUY','Izibank', "G98",g)
        insertvalue('SHIB',100000,'BUY','Izibank', "H98",g)
        matrix.append(g)
        wks1.update_values('B92:H98', matrix ) 
        
        


         



    BUYUAH()




while True:
    newmain()
    time.sleep(200)
    pass