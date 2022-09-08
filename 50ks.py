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
        insertvalue('USDT',50000,'BUY','PrivatBank', "B64",a)
       
        insertvalue('BTC',50000,'BUY','PrivatBank', "C64",a)
       
        insertvalue('BUSD',50000,'BUY','PrivatBank', "D64",a)
        
        insertvalue('BNB',50000,'BUY','PrivatBank', "E64",a)
        insertvalue('ETH',50000,'BUY','PrivatBank', "F64",a)
        insertvalue('UAH',50000,'BUY','PrivatBank', "G64",a)
        insertvalue('SHIB',50000,'BUY','PrivatBank', "H64",a)
        matrix.append(a)
        
        
        insertvalue('USDT',50000,'BUY','Monobank', "B65",b)
        insertvalue('BTC',50000,'BUY','Monobank', "C65",b)
        insertvalue('BUSD',50000,'BUY','Monobank', "D65",b)
        insertvalue('BNB',50000,'BUY','Monobank', "E65",b)
        insertvalue('ETH',50000,'BUY','Monobank', "F65",b)
        insertvalue('UAH',50000,'BUY','Monobank', "G65",b)
        insertvalue('SHIB',50000,'BUY','Monobank', "H65",b)
        matrix.append(b)
         
        
        insertvalue('USDT',50000,'BUY','UAHfiatbalance', "B66",c)
        insertvalue('BTC',50000,'BUY','UAHfiatbalance', "C66",c)
        insertvalue('BUSD',50000,'BUY','UAHfiatbalance', "D66",c)
        insertvalue('BNB',50000,'BUY','UAHfiatbalance', "E66",c)
        insertvalue('ETH',50000,'BUY','UAHfiatbalance', "F66",c)
        insertvalue('UAH',50000,'BUY','UAHfiatbalance', "G66",c)
        insertvalue('SHIB',50000,'BUY','UAHfiatbalance', "H66",c)
        matrix.append(c)
        insertvalue('USDT',50000,'BUY','ABank', "B67",d)
        insertvalue('BTC',50000,'BUY','ABank', "C67",d)
        insertvalue('BUSD',50000,'BUY','ABank', "D67",d)
        insertvalue('BNB',50000,'BUY','ABank', "E67",d)
        insertvalue('ETH',50000,'BUY','ABank', "F67",d)
        insertvalue('UAH',50000,'BUY','ABank', "G67",d)
        insertvalue('SHIB',50000,'BUY','ABank', "H67",d)
        matrix.append(d)
        insertvalue('USDT',50000,'BUY','Pumbbank', "B68",e)
        insertvalue('BTC',50000,'BUY','Pumbbank', "C68",e)
        insertvalue('BUSD',50000,'BUY','Pumbbank', "D68",e)
        insertvalue('BNB',50000,'BUY','Pumbbank', "E68",e)
        insertvalue('ETH',50000,'BUY','Pumbbank', "F68",e)
        insertvalue('UAH',50000,'BUY','Pumbbank', "G68",e)
        insertvalue('SHIB',50000,'BUY','Pumbbank', "H68",e)
        matrix.append(e)
        
        insertvalue('USDT',50000,'BUY','Sportbank', "B69",f)
        insertvalue('BTC',50000,'BUY','Sportbank', "C69",f)
        insertvalue('BUSD',50000,'BUY','Sportbank', "D69",f)
        insertvalue('BNB',50000,'BUY','Sportbank', "E69",f)
        insertvalue('ETH',50000,'BUY','Sportbank', "F69",f)
        insertvalue('UAH',50000,'BUY','Sportbank', "G69",f)
        insertvalue('SHIB',50000,'BUY','Sportbank', "H69",f)
        matrix.append(f)
        
        
        insertvalue('USDT',50000,'BUY','Izibank', "B70",g)
        insertvalue('BTC',50000,'BUY','Izibank', "C70",g)
        insertvalue('BUSD',50000,'BUY','Izibank', "D70",g)
        insertvalue('BNB',50000,'BUY','Izibank', "E70",g)
        insertvalue('ETH',50000,'BUY','Izibank', "F70",g)
        insertvalue('UAH',50000,'BUY','Izibank', "G70",g)
        insertvalue('SHIB',50000,'BUY','Izibank', "H70",g)
        matrix.append(g)
        wks1.update_values('B64:H70', matrix ) 
        
        


         




    BUYUAH()

while True:
    newmain()
    time.sleep(200)
    pass

