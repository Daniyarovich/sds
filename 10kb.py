import pygsheets
import sys 
import numpy as np
import requests
import time
gc = pygsheets.authorize(client_secret='token1.json')
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
    # share the sheet with your friend

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
        insertvalue('USDT',10000,'SELL','PrivatBank', "B36",a)
       
        insertvalue('BTC',10000,'SELL','PrivatBank', "C36",a)
       
        insertvalue('BUSD',10000,'SELL','PrivatBank', "D36",a)
        
        insertvalue('BNB',10000,'SELL','PrivatBank', "E36",a)
        insertvalue('ETH',10000,'SELL','PrivatBank', "F36",a)
        insertvalue('UAH',10000,'SELL','PrivatBank', "G36",a)
        insertvalue('SHIB',10000,'SELL','PrivatBank', "H36",a)
        matrix.append(a)
        
        insertvalue('USDT',10000,'SELL','Monobank', "B37",b)
        insertvalue('BTC',10000,'SELL','Monobank', "C37",b)
        insertvalue('BUSD',10000,'SELL','Monobank', "D37",b)
        insertvalue('BNB',10000,'SELL','Monobank', "E37",b)
        insertvalue('ETH',10000,'SELL','Monobank', "F37",b)
        insertvalue('UAH',10000,'SELL','Monobank', "G37",b)
        insertvalue('SHIB',10000,'SELL','Monobank', "H37",b)
        matrix.append(b)
         
        
        insertvalue('USDT',10000,'SELL','UAHfiatbalance', "B38",c)
        insertvalue('BTC',10000,'SELL','UAHfiatbalance', "C38",c)
        insertvalue('BUSD',10000,'SELL','UAHfiatbalance', "D38",c)
        insertvalue('BNB',10000,'SELL','UAHfiatbalance', "E38",c)
        insertvalue('ETH',10000,'SELL','UAHfiatbalance', "F38",c)
        insertvalue('UAH',10000,'SELL','UAHfiatbalance', "G38",c)
        insertvalue('SHIB',10000,'SELL','UAHfiatbalance', "H38",c)
        matrix.append(c)
        insertvalue('USDT',10000,'SELL','ABank', "B39",d)
        insertvalue('BTC',10000,'SELL','ABank', "C39",d)
        insertvalue('BUSD',10000,'SELL','ABank', "D39",d)
        insertvalue('BNB',10000,'SELL','ABank', "E39",d)
        insertvalue('ETH',10000,'SELL','ABank', "F39",d)
        insertvalue('UAH',10000,'SELL','ABank', "G39",d)
        insertvalue('SHIB',10000,'SELL','ABank', "H39",d)
        matrix.append(d)
        insertvalue('USDT',10000,'SELL','Pumbbank', "B40",e)
        insertvalue('BTC',10000,'SELL','Pumbbank', "C40",e)
        insertvalue('BUSD',10000,'SELL','Pumbbank', "D40",e)
        insertvalue('BNB',10000,'SELL','Pumbbank', "E40",e)
        insertvalue('ETH',10000,'SELL','Pumbbank', "F40",e)
        insertvalue('UAH',10000,'SELL','Pumbbank', "G40",e)
        insertvalue('SHIB',10000,'SELL','Pumbbank', "H40",e)
        matrix.append(e)
        
        insertvalue('USDT',10000,'SELL','Sportbank', "B41",f)
        insertvalue('BTC',10000,'SELL','Sportbank', "C41",f)
        insertvalue('BUSD',10000,'SELL','Sportbank', "D41",f)
        insertvalue('BNB',10000,'SELL','Sportbank', "E41",f)
        insertvalue('ETH',10000,'SELL','Sportbank', "F41",f)
        insertvalue('UAH',10000,'SELL','Sportbank', "G41",f)
        insertvalue('SHIB',10000,'SELL','Sportbank', "H41",f)
        matrix.append(f)
        
        
        insertvalue('USDT',10000,'SELL','Izibank', "B42",g)
        insertvalue('BTC',10000,'SELL','Izibank', "C42",g)
        insertvalue('BUSD',10000,'SELL','Izibank', "D42",g)
        insertvalue('BNB',10000,'SELL','Izibank', "E42",g)
        insertvalue('ETH',10000,'SELL','Izibank', "F42",g)
        insertvalue('UAH',10000,'SELL','Izibank', "G42",g)
        insertvalue('SHIB',10000,'SELL','Izibank', "H42",g)
        matrix.append(g)
        wks1.update_values('B36:H42', matrix ) 
        
        


         



    SELLUAH()
while True:
    newmain()
    time.sleep(200)
    pass    



