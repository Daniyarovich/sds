import pygsheets
import numpy as np
import requests
import sys 
import time
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

    def BUYUAH():
        insertvalue('USDT',1000,'BUY','PrivatBank', "B22",a)
       
        insertvalue('BTC',1000,'BUY','PrivatBank', "C22",a)
       
        insertvalue('BUSD',1000,'BUY','PrivatBank', "D22",a)
        
        insertvalue('BNB',1000,'BUY','PrivatBank', "E22",a)
        insertvalue('ETH',1000,'BUY','PrivatBank', "F22",a)
        insertvalue('UAH',1000,'BUY','PrivatBank', "G22",a)
        insertvalue('SHIB',1000,'BUY','PrivatBank', "H22",a)
        matrix.append(a)
        
        
        insertvalue('USDT',1000,'BUY','Monobank', "B23",b)
        insertvalue('BTC',1000,'BUY','Monobank', "C23",b)
        insertvalue('BUSD',1000,'BUY','Monobank', "D23",b)
        insertvalue('BNB',1000,'BUY','Monobank', "E23",b)
        insertvalue('ETH',1000,'BUY','Monobank', "F23",b)
        insertvalue('UAH',1000,'BUY','Monobank', "G23",b)
        insertvalue('SHIB',1000,'BUY','Monobank', "H23",b)
        matrix.append(b)
         
        
        insertvalue('USDT',1000,'BUY','UAHfiatbalance', "B24",c)
        insertvalue('BTC',1000,'BUY','UAHfiatbalance', "C24",c)
        insertvalue('BUSD',1000,'BUY','UAHfiatbalance', "D24",c)
        insertvalue('BNB',1000,'BUY','UAHfiatbalance', "E24",c)
        insertvalue('ETH',1000,'BUY','UAHfiatbalance', "F24",c)
        insertvalue('UAH',1000,'BUY','UAHfiatbalance', "G24",c)
        insertvalue('SHIB',1000,'BUY','UAHfiatbalance', "H24",c)
        matrix.append(c)
        insertvalue('USDT',1000,'BUY','ABank', "B25",d)
        insertvalue('BTC',1000,'BUY','ABank', "C25",d)
        insertvalue('BUSD',1000,'BUY','ABank', "D25",d)
        insertvalue('BNB',1000,'BUY','ABank', "E25",d)
        insertvalue('ETH',1000,'BUY','ABank', "F25",d)
        insertvalue('UAH',1000,'BUY','ABank', "G25",d)
        insertvalue('SHIB',1000,'BUY','ABank', "H25",d)
        matrix.append(d)
        insertvalue('USDT',1000,'BUY','Pumbbank', "B26",e)
        insertvalue('BTC',1000,'BUY','Pumbbank', "C26",e)
        insertvalue('BUSD',1000,'BUY','Pumbbank', "D26",e)
        insertvalue('BNB',1000,'BUY','Pumbbank', "E26",e)
        insertvalue('ETH',1000,'BUY','Pumbbank', "F26",e)
        insertvalue('UAH',1000,'BUY','Pumbbank', "G26",e)
        insertvalue('SHIB',1000,'BUY','Pumbbank', "H26",e)
        matrix.append(e)
        
        insertvalue('USDT',1000,'BUY','Sportbank', "B27",f)
        insertvalue('BTC',1000,'BUY','Sportbank', "C27",f)
        insertvalue('BUSD',1000,'BUY','Sportbank', "D27",f)
        insertvalue('BNB',1000,'BUY','Sportbank', "E27",f)
        insertvalue('ETH',1000,'BUY','Sportbank', "F27",f)
        insertvalue('UAH',1000,'BUY','Sportbank', "G27",f)
        insertvalue('SHIB',1000,'BUY','Sportbank', "H27",f)
        matrix.append(f)
        
        
        insertvalue('USDT',1000,'BUY','Izibank', "B28",g)
        insertvalue('BTC',1000,'BUY','Izibank', "C28",g)
        insertvalue('BUSD',1000,'BUY','Izibank', "D28",g)
        insertvalue('BNB',1000,'BUY','Izibank', "E28",g)
        insertvalue('ETH',1000,'BUY','Izibank', "F28",g)
        insertvalue('UAH',1000,'BUY','Izibank', "G28",g)
        insertvalue('SHIB',1000,'BUY','Izibank', "H28",g)
        matrix.append(g)
        wks1.update_values('B22:H28', matrix ) 
        
        


         



    BUYUAH()
while True:
    newmain()
    time.sleep(200)
    pass    



