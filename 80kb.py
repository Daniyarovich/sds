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
        insertvalue('USDT',80000,'SELL','PrivatBank', "B78",a)
       
        insertvalue('BTC',80000,'SELL','PrivatBank', "C78",a)
       
        insertvalue('BUSD',80000,'SELL','PrivatBank', "D78",a)
        
        insertvalue('BNB',80000,'SELL','PrivatBank', "E78",a)
        insertvalue('ETH',80000,'SELL','PrivatBank', "F78",a)
        insertvalue('UAH',80000,'SELL','PrivatBank', "G78",a)
        insertvalue('SHIB',80000,'SELL','PrivatBank', "H78",a)
        matrix.append(a)
        
        
        insertvalue('USDT',80000,'SELL','Monobank', "B79",b)
        insertvalue('BTC',80000,'SELL','Monobank', "C79",b)
        insertvalue('BUSD',80000,'SELL','Monobank', "D79",b)
        insertvalue('BNB',80000,'SELL','Monobank', "E79",b)
        insertvalue('ETH',80000,'SELL','Monobank', "F79",b)
        insertvalue('UAH',80000,'SELL','Monobank', "G79",b)
        insertvalue('SHIB',80000,'SELL','Monobank', "H79",b)
        matrix.append(b)
         
        
        insertvalue('USDT',80000,'SELL','UAHfiatbalance', "B80",c)
        insertvalue('BTC',80000,'SELL','UAHfiatbalance', "C80",c)
        insertvalue('BUSD',80000,'SELL','UAHfiatbalance', "D80",c)
        insertvalue('BNB',80000,'SELL','UAHfiatbalance', "E80",c)
        insertvalue('ETH',80000,'SELL','UAHfiatbalance', "F80",c)
        insertvalue('UAH',80000,'SELL','UAHfiatbalance', "G80",c)
        insertvalue('SHIB',80000,'SELL','UAHfiatbalance', "H80",c)
        matrix.append(c)
        insertvalue('USDT',80000,'SELL','ABank', "B81",d)
        insertvalue('BTC',80000,'SELL','ABank', "C81",d)
        insertvalue('BUSD',80000,'SELL','ABank', "D81",d)
        insertvalue('BNB',80000,'SELL','ABank', "E81",d)
        insertvalue('ETH',80000,'SELL','ABank', "F81",d)
        insertvalue('UAH',80000,'SELL','ABank', "G81",d)
        insertvalue('SHIB',80000,'SELL','ABank', "H81",d)
        matrix.append(d)
        insertvalue('USDT',80000,'SELL','Pumbbank', "B82",e)
        insertvalue('BTC',80000,'SELL','Pumbbank', "C82",e)
        insertvalue('BUSD',80000,'SELL','Pumbbank', "D82",e)
        insertvalue('BNB',80000,'SELL','Pumbbank', "E82",e)
        insertvalue('ETH',80000,'SELL','Pumbbank', "F82",e)
        insertvalue('UAH',80000,'SELL','Pumbbank', "G82",e)
        insertvalue('SHIB',80000,'SELL','Pumbbank', "H82",e)
        matrix.append(e)
        
        insertvalue('USDT',80000,'SELL','Sportbank', "B83",f)
        insertvalue('BTC',80000,'SELL','Sportbank', "C83",f)
        insertvalue('BUSD',80000,'SELL','Sportbank', "D83",f)
        insertvalue('BNB',80000,'SELL','Sportbank', "E83",f)
        insertvalue('ETH',80000,'SELL','Sportbank', "F83",f)
        insertvalue('UAH',80000,'SELL','Sportbank', "G83",f)
        insertvalue('SHIB',80000,'SELL','Sportbank', "H83",f)
        matrix.append(f)
        
        
        insertvalue('USDT',80000,'SELL','Izibank', "B84",g)
        insertvalue('BTC',80000,'SELL','Izibank', "C84",g)
        insertvalue('BUSD',80000,'SELL','Izibank', "D84",g)
        insertvalue('BNB',80000,'SELL','Izibank', "E84",g)
        insertvalue('ETH',80000,'SELL','Izibank', "F84",g)
        insertvalue('UAH',80000,'SELL','Izibank', "G84",g)
        insertvalue('SHIB',80000,'SELL','Izibank', "H84",g)
        matrix.append(g)
        wks1.update_values('B78:H84', matrix ) 
        
        


         

    SELLUAH()
while True:
    newmain()
    time.sleep(200)
    pass    