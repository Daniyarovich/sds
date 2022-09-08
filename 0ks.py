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
        insertvalue('USDT',0,'BUY','PrivatBank', "B8",a)
       
        insertvalue('BTC',0,'BUY','PrivatBank', "C8",a)
       
        insertvalue('BUSD',0,'BUY','PrivatBank', "D8",a)
        
        insertvalue('BNB',0,'BUY','PrivatBank', "E8",a)
        insertvalue('ETH',0,'BUY','PrivatBank', "F8",a)
        insertvalue('UAH',0,'BUY','PrivatBank', "G8",a)
        insertvalue('SHIB',0,'BUY','PrivatBank', "H8",a)
        matrix.append(a)
        
        
        insertvalue('USDT',0,'BUY','Monobank', "B9",b)
        insertvalue('BTC',0,'BUY','Monobank', "C9",b)
        insertvalue('BUSD',0,'BUY','Monobank', "D9",b)
        insertvalue('BNB',0,'BUY','Monobank', "E9",b)
        insertvalue('ETH',0,'BUY','Monobank', "F9",b)
        insertvalue('UAH',0,'BUY','Monobank', "G9",b)
        insertvalue('SHIB',0,'BUY','Monobank', "H9",b)
        matrix.append(b)
         
        
        insertvalue('USDT',0,'BUY','UAHfiatbalance', "B10",c)
        insertvalue('BTC',0,'BUY','UAHfiatbalance', "C10",c)
        insertvalue('BUSD',0,'BUY','UAHfiatbalance', "D10",c)
        insertvalue('BNB',0,'BUY','UAHfiatbalance', "E10",c)
        insertvalue('ETH',0,'BUY','UAHfiatbalance', "F10",c)
        insertvalue('UAH',0,'BUY','UAHfiatbalance', "G10",c)
        insertvalue('SHIB',0,'BUY','UAHfiatbalance', "H10",c)
        matrix.append(c)
        insertvalue('USDT',0,'BUY','ABank', "B11",d)
        insertvalue('BTC',0,'BUY','ABank', "C11",d)
        insertvalue('BUSD',0,'BUY','ABank', "D11",d)
        insertvalue('BNB',0,'BUY','ABank', "E11",d)
        insertvalue('ETH',0,'BUY','ABank', "F11",d)
        insertvalue('UAH',0,'BUY','ABank', "G11",d)
        insertvalue('SHIB',0,'BUY','ABank', "H11",d)
        matrix.append(d)
        insertvalue('USDT',0,'BUY','Pumbbank', "B12",e)
        insertvalue('BTC',0,'BUY','Pumbbank', "C12",e)
        insertvalue('BUSD',0,'BUY','Pumbbank', "D12",e)
        insertvalue('BNB',0,'BUY','Pumbbank', "E12",e)
        insertvalue('ETH',0,'BUY','Pumbbank', "F12",e)
        insertvalue('UAH',0,'BUY','Pumbbank', "G12",e)
        insertvalue('SHIB',0,'BUY','Pumbbank', "H12",e)
        matrix.append(e)
        
        insertvalue('USDT',0,'BUY','Sportbank', "B13",f)
        insertvalue('BTC',0,'BUY','Sportbank', "C13",f)
        insertvalue('BUSD',0,'BUY','Sportbank', "D13",f)
        insertvalue('BNB',0,'BUY','Sportbank', "E13",f)
        insertvalue('ETH',0,'BUY','Sportbank', "F13",f)
        insertvalue('UAH',0,'BUY','Sportbank', "G13",f)
        insertvalue('SHIB',0,'BUY','Sportbank', "H13",f)
        matrix.append(f)
        
        
        insertvalue('USDT',0,'BUY','Izibank', "B14",g)
        insertvalue('BTC',0,'BUY','Izibank', "C14",g)
        insertvalue('BUSD',0,'BUY','Izibank', "D14",g)
        insertvalue('BNB',0,'BUY','Izibank', "E14",g)
        insertvalue('ETH',0,'BUY','Izibank', "F14",g)
        insertvalue('UAH',0,'BUY','Izibank', "G14",g)
        insertvalue('SHIB',0,'BUY','Izibank', "H14",g)
        matrix.append(g)
        
        wks1.update_values('B8:H14', matrix ) 
        
        


         


    BUYUAH()



while True:
    newmain()
    time.sleep(200)
    pass








