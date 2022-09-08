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
        insertvalue('USDT',50000,'SELL','PrivatBank', "B64",a)
       
        insertvalue('BTC',50000,'SELL','PrivatBank', "C64",a)
       
        insertvalue('BUSD',50000,'SELL','PrivatBank', "D64",a)
        
        insertvalue('BNB',50000,'SELL','PrivatBank', "E64",a)
        insertvalue('ETH',50000,'SELL','PrivatBank', "F64",a)
        insertvalue('UAH',50000,'SELL','PrivatBank', "G64",a)
        insertvalue('SHIB',50000,'SELL','PrivatBank', "H64",a)
        matrix.append(a)
        
        
        insertvalue('USDT',50000,'SELL','Monobank', "B65",b)
        insertvalue('BTC',50000,'SELL','Monobank', "C65",b)
        insertvalue('BUSD',50000,'SELL','Monobank', "D65",b)
        insertvalue('BNB',50000,'SELL','Monobank', "E65",b)
        insertvalue('ETH',50000,'SELL','Monobank', "F65",b)
        insertvalue('UAH',50000,'SELL','Monobank', "G65",b)
        insertvalue('SHIB',50000,'SELL','Monobank', "H65",b)
        matrix.append(b)
         
        
        insertvalue('USDT',50000,'SELL','UAHfiatbalance', "B66",c)
        insertvalue('BTC',50000,'SELL','UAHfiatbalance', "C66",c)
        insertvalue('BUSD',50000,'SELL','UAHfiatbalance', "D66",c)
        insertvalue('BNB',50000,'SELL','UAHfiatbalance', "E66",c)
        insertvalue('ETH',50000,'SELL','UAHfiatbalance', "F66",c)
        insertvalue('UAH',50000,'SELL','UAHfiatbalance', "G66",c)
        insertvalue('SHIB',50000,'SELL','UAHfiatbalance', "H66",c)
        matrix.append(c)
        insertvalue('USDT',50000,'SELL','ABank', "B67",d)
        insertvalue('BTC',50000,'SELL','ABank', "C67",d)
        insertvalue('BUSD',50000,'SELL','ABank', "D67",d)
        insertvalue('BNB',50000,'SELL','ABank', "E67",d)
        insertvalue('ETH',50000,'SELL','ABank', "F67",d)
        insertvalue('UAH',50000,'SELL','ABank', "G67",d)
        insertvalue('SHIB',50000,'SELL','ABank', "H67",d)
        matrix.append(d)
        insertvalue('USDT',50000,'SELL','Pumbbank', "B68",e)
        insertvalue('BTC',50000,'SELL','Pumbbank', "C68",e)
        insertvalue('BUSD',50000,'SELL','Pumbbank', "D68",e)
        insertvalue('BNB',50000,'SELL','Pumbbank', "E68",e)
        insertvalue('ETH',50000,'SELL','Pumbbank', "F68",e)
        insertvalue('UAH',50000,'SELL','Pumbbank', "G68",e)
        insertvalue('SHIB',50000,'SELL','Pumbbank', "H68",e)
        matrix.append(e)
        
        insertvalue('USDT',50000,'SELL','Sportbank', "B69",f)
        insertvalue('BTC',50000,'SELL','Sportbank', "C69",f)
        insertvalue('BUSD',50000,'SELL','Sportbank', "D69",f)
        insertvalue('BNB',50000,'SELL','Sportbank', "E69",f)
        insertvalue('ETH',50000,'SELL','Sportbank', "F69",f)
        insertvalue('UAH',50000,'SELL','Sportbank', "G69",f)
        insertvalue('SHIB',50000,'SELL','Sportbank', "H69",f)
        matrix.append(f)
        
        
        insertvalue('USDT',50000,'SELL','Izibank', "B70",g)
        insertvalue('BTC',50000,'SELL','Izibank', "C70",g)
        insertvalue('BUSD',50000,'SELL','Izibank', "D70",g)
        insertvalue('BNB',50000,'SELL','Izibank', "E70",g)
        insertvalue('ETH',50000,'SELL','Izibank', "F70",g)
        insertvalue('UAH',50000,'SELL','Izibank', "G70",g)
        insertvalue('SHIB',50000,'SELL','Izibank', "H70",g)
        matrix.append(g)
        wks1.update_values('B64:H70', matrix ) 
        
        


         

    SELLUAH()
while True:
    newmain()
    time.sleep(200)
    pass    




