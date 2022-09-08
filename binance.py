import pygsheets
import numpy as np
import requests
import math
gc = pygsheets.authorize(client_secret='token.json')
sh = gc.open('Binance 2.0')
wks = sh.worksheet_by_title("Маркет")
wks1 = sh.worksheet_by_title("UAH - BUY")
wks2 = sh.worksheet_by_title("UAH - SELL")
wks3 = sh.worksheet_by_title("Test")
# Update a cell with value (just to let him know valu
# update the sheet with array

# share the sheet with your friend

def delete_zeros(value: float):
    while not value % 10:
        value //= 10
    return value
def insertvalue(asset, amount, tradetype, bank, row):
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
        wks1.update_value(row, line )         
    except:
        wks1.update_value(row, "Пусто" ) 
def insertvalue1(asset, amount, tradetype, bank, row):
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
        wks2.update_value(row, line )        
    except:
        wks2.update_value(row, "Пусто" ) 
    
def getMarketPrice():
    headers = {
    "Accept": "*/*",

    "content-type": "application/json",
    }

    response = requests.get("https://www.binance.com/api/v3/ticker/price", headers=headers)
    sp = response.text;
    spBusdUah = sp.split('BUSDUAH');
    spUsdtUah = sp.split('BUSDUAH');
    spBtcUah= sp.split('BTCUAH');
    spBnbUah = sp.split('BNBUAH');
    spEthUah = sp.split('ETHUAH');
    spShibUah= sp.split('SHIBUAH');
  
    spBusdEth = sp.split('ETHBUSD');
    spUsdtEth = sp.split('ETHUSDT');
    spBtcEth= sp.split('ETHBTC');
    spBnbEth = sp.split('BNBETH');
    spUahEth = sp.split('ETHUAH');
  
  
  
    spUsdtBnb = sp.split('BNBUSDT');
    spBtcBnb= sp.split('BNBBTC');
  
    spBtcBusd= sp.split('BTCBUSD');
    spShibBusd= sp.split('SHIBBUSD');
    spBtcUsdt= sp.split('BTCUSDT');
    spShibUsdt= sp.split('SHIBUSDT');

  
    inBusdUah = spBusdUah[1].split('"');
    inUsdtUah = spUsdtUah[1].split('"');
    inBtcUah = spBtcUah[1].split('"');
    inBnbUah = spBnbUah[1].split('"');
    inEthUah = spEthUah[1].split('"');
    inShibUah = spShibUah[1].split('"');
    inShibUsdt = spShibUsdt[1].split('"');
    inBusdEth = spBusdEth[1].split('"');
    inUsdtEth = spUsdtEth[1].split('"');
    inBtcEth = spBtcEth[1].split('"');
    inBnbEth = spBnbEth[1].split('"');
    inUahEth = spUahEth[1].split('"');

    inUsdtBnb = spUsdtBnb[1].split('"');
    inBtcBnb = spBtcBnb[1].split('"');

    inBtcBusd = spBtcBusd[1].split('"');
    inShibBusd = spShibBusd[1].split('"');

    inBtcUsdt = spBtcUsdt[1].split('"');
    wks.update_value('G9', delete_zeros(float(inBusdUah[4]) ))
    wks.update_value('C7', delete_zeros(float(inBtcUsdt[4]) ))
    wks.update_value('B8', delete_zeros(float(inBtcUsdt[4]) ))
    wks.update_value('B10', delete_zeros(float(inUsdtBnb[4]) ))
    wks.update_value('B11', delete_zeros(float(inUsdtEth[4]) ))
    wks.update_value('B12', delete_zeros(float(inUsdtUah[4]) ))
    wks.update_value('C9', delete_zeros(float(inBtcBusd[4]) ))
    wks.update_value('C10', delete_zeros(float(inBtcBnb[4]) ))
    wks.update_value('C11', delete_zeros(float(inBtcEth[4]) ))
    wks.update_value('C12', delete_zeros(float(inBtcUah[4]) ))
    wks.update_value('D8', delete_zeros(float(inBtcBusd[4]) ))
    wks.update_value('D10', delete_zeros(float(inUsdtBnb[4]) ))
    wks.update_value('D11', delete_zeros(float(inBusdEth[4]) ))
    wks.update_value('D12', delete_zeros(float(inBusdUah[4]) ))
    wks.update_value('E7', delete_zeros(float(inUsdtBnb[4]) ))
    wks.update_value('E8', delete_zeros(float(inBtcBnb[4]) ))
    wks.update_value('E9', delete_zeros(float(inUsdtBnb[4]) ))
    wks.update_value('E11', delete_zeros(float(inBnbEth[4]) ))
    wks.update_value('E12', delete_zeros(float(inBnbUah[4]) ))
    wks.update_value('F7', delete_zeros(float(inUsdtEth[4]) ))
    wks.update_value('F8', delete_zeros(float(inBtcEth[4]) ))
    wks.update_value('F10', delete_zeros(float(inBnbEth[4]) ))
    wks.update_value('F9', delete_zeros(float(inBusdEth[4]) ))
    wks.update_value('F12', delete_zeros(float(inEthUah[4]) ))
    wks.update_value('G7', delete_zeros(float(inUsdtUah[4]) ))
    wks.update_value('G8', delete_zeros(float(inBtcUah[4]) ))
    wks.update_value('G9', delete_zeros(float(inBusdUah[4]) ))
    wks.update_value('G10', delete_zeros(float(inBnbUah[4]) ))
    wks.update_value('G11', delete_zeros(float(inEthUah[4]) ))
    wks.update_value('H7', delete_zeros(float(inShibUsdt[4]) ))
    wks.update_value('H9', delete_zeros(float(inShibBusd[4]) ))
    wks.update_value('H12', delete_zeros(float(inShibUah[4]) ))
def BUYUAH():
    insertvalue('USDT',0,'BUY','PrivatBank', "B8")
    insertvalue('BTC',0,'BUY','PrivatBank', "C8")
    insertvalue('BUSD',0,'BUY','PrivatBank', "D8")
    insertvalue('BNB',0,'BUY','PrivatBank', "E8")
    insertvalue('ETH',0,'BUY','PrivatBank', "F8")
    insertvalue('UAH',0,'BUY','PrivatBank', "G8")
    insertvalue('SHIB',0,'BUY','PrivatBank', "H8")

    insertvalue('USDT',0,'BUY','Monobank', "B9")
    insertvalue('BTC',0,'BUY','Monobank', "C9")
    insertvalue('BUSD',0,'BUY','Monobank', "D9")
    insertvalue('BNB',0,'BUY','Monobank', "E9")
    insertvalue('ETH',0,'BUY','Monobank', "F9")
    insertvalue('UAH',0,'BUY','Monobank', "G9")
    insertvalue('SHIB',0,'BUY','Monobank', "H9")
   
    insertvalue('USDT',0,'BUY','ABank', "B11")
    insertvalue('BTC',0,'BUY','ABank', "C11")
    insertvalue('BUSD',0,'BUY','ABank', "D11")
    insertvalue('BNB',0,'BUY','ABank', "E11")
    insertvalue('ETH',0,'BUY','ABank', "F11")
    insertvalue('UAH',0,'BUY','ABank', "G11")
    insertvalue('SHIB',0,'BUY','ABank', "H11")

    insertvalue('USDT',0,'BUY','Pumbbank', "B12")
    insertvalue('BTC',0,'BUY','Pumbbank', "C12")
    insertvalue('BUSD',0,'BUY','Pumbbank', "D12")
    insertvalue('BNB',0,'BUY','Pumbbank', "E12")
    insertvalue('ETH',0,'BUY','Pumbbank', "F12")
    insertvalue('UAH',0,'BUY','Pumbbank', "G12")
    insertvalue('SHIB',0,'BUY','Pumbbank', "H12")

    insertvalue('USDT',0,'BUY','Sportbank', "B13")
    insertvalue('BTC',0,'BUY','Sportbank', "C13")
    insertvalue('BUSD',0,'BUY','Sportbank', "D13")
    insertvalue('BNB',0,'BUY','Sportbank', "E13")
    insertvalue('ETH',0,'BUY','Sportbank', "F13")
    insertvalue('UAH',0,'BUY','Sportbank', "G13")
    insertvalue('SHIB',0,'BUY','Sportbank', "H13")


    insertvalue('USDT',0,'BUY','Izibank', "B14")
    insertvalue('BTC',0,'BUY','Izibank', "C14")
    insertvalue('BUSD',0,'BUY','Izibank', "D14")
    insertvalue('BNB',0,'BUY','Izibank', "E14")
    insertvalue('ETH',0,'BUY','Izibank', "F14")
    insertvalue('UAH',0,'BUY','Izibank', "G14")
    insertvalue('SHIB',0,'BUY','Izibank', "H14")


    insertvalue('USDT',1000,'BUY','PrivatBank', "B22")
    insertvalue('BTC',1000,'BUY','PrivatBank', "C22")
    insertvalue('BUSD',1000,'BUY','PrivatBank', "D22")
    insertvalue('BNB',1000,'BUY','PrivatBank', "E22")
    insertvalue('ETH',1000,'BUY','PrivatBank', "F22")
    insertvalue('UAH',1000,'BUY','PrivatBank', "G22")
    insertvalue('SHIB',1000,'BUY','PrivatBank', "H22")

    insertvalue('USDT',1000,'BUY','Monobank', "B23")
    insertvalue('BTC',1000,'BUY','Monobank', "C23")
    insertvalue('BUSD',1000,'BUY','Monobank', "D23")
    insertvalue('BNB',1000,'BUY','Monobank', "E23")
    insertvalue('ETH',1000,'BUY','Monobank', "F23")
    insertvalue('UAH',1000,'BUY','Monobank', "G23")
    insertvalue('SHIB',1000,'BUY','Monobank', "H23")

    insertvalue('USDT',1000,'BUY','ABank', "B25")
    insertvalue('BTC',1000,'BUY','ABank', "C25")
    insertvalue('BUSD',1000,'BUY','ABank', "D25")
    insertvalue('BNB',1000,'BUY','ABank', "E25")
    insertvalue('ETH',1000,'BUY','ABank', "F25")
    insertvalue('UAH',1000,'BUY','ABank', "G25")
    insertvalue('SHIB',1000,'BUY','ABank', "H25")

    insertvalue('USDT',1000,'BUY','Pumbbank', "B26")
    insertvalue('BTC',1000,'BUY','Pumbbank', "C26")
    insertvalue('BUSD',1000,'BUY','Pumbbank', "D26")
    insertvalue('BNB',1000,'BUY','Pumbbank', "E26")
    insertvalue('ETH',1000,'BUY','Pumbbank', "F26")
    insertvalue('UAH',1000,'BUY','Pumbbank', "G26")
    insertvalue('SHIB',1000,'BUY','Pumbbank', "H26")

    insertvalue('USDT',1000,'BUY','Sportbank', "B27")
    insertvalue('BTC',1000,'BUY','Sportbank', "C27")
    insertvalue('BUSD',1000,'BUY','Sportbank', "D27")
    insertvalue('BNB',1000,'BUY','Sportbank', "E27")
    insertvalue('ETH',1000,'BUY','Sportbank', "F27")
    insertvalue('UAH',1000,'BUY','Sportbank', "G27")
    insertvalue('SHIB',1000,'BUY','Sportbank', "H27")


    insertvalue('USDT',1000,'BUY','Izibank', "B28")
    insertvalue('BTC',1000,'BUY','Izibank', "C28")
    insertvalue('BUSD',1000,'BUY','Izibank', "D28")
    insertvalue('BNB',1000,'BUY','Izibank', "E28")
    insertvalue('ETH',1000,'BUY','Izibank', "F28")
    insertvalue('UAH',1000,'BUY','Izibank', "G28")
    insertvalue('SHIB',1000,'BUY','Izibank', "H28")


    insertvalue('USDT',10000,'BUY','PrivatBank', "B36")
    insertvalue('BTC',10000,'BUY','PrivatBank', "C36")
    insertvalue('BUSD',10000,'BUY','PrivatBank', "D36")
    insertvalue('BNB',10000,'BUY','PrivatBank', "E36")
    insertvalue('ETH',10000,'BUY','PrivatBank', "F36")
    insertvalue('UAH',10000,'BUY','PrivatBank', "G36")
    insertvalue('SHIB',10000,'BUY','PrivatBank', "H36")

    insertvalue('USDT',10000,'BUY','Monobank', "B37")
    insertvalue('BTC',10000,'BUY','Monobank', "C37")
    insertvalue('BUSD',10000,'BUY','Monobank', "D37")
    insertvalue('BNB',10000,'BUY','Monobank', "E37")
    insertvalue('ETH',10000,'BUY','Monobank', "F37")
    insertvalue('UAH',10000,'BUY','Monobank', "G37")
    insertvalue('SHIB',10000,'BUY','Monobank', "H37")

    insertvalue('USDT',10000,'BUY','ABank', "B39")
    insertvalue('BTC',10000,'BUY','ABank', "C39")
    insertvalue('BUSD',10000,'BUY','ABank', "D39")
    insertvalue('BNB',10000,'BUY','ABank', "E39")
    insertvalue('ETH',10000,'BUY','ABank', "F39")
    insertvalue('UAH',10000,'BUY','ABank', "G39")
    insertvalue('SHIB',10000,'BUY','ABank', "H39")

    insertvalue('USDT',10000,'BUY','Pumbbank', "B40")
    insertvalue('BTC',10000,'BUY','Pumbbank', "C40")
    insertvalue('BUSD',10000,'BUY','Pumbbank', "D40")
    insertvalue('BNB',10000,'BUY','Pumbbank', "E40")
    insertvalue('ETH',10000,'BUY','Pumbbank', "F40")
    insertvalue('UAH',10000,'BUY','Pumbbank', "G40")
    insertvalue('SHIB',10000,'BUY','Pumbbank', "H40")

    insertvalue('USDT',10000,'BUY','Sportbank', "B41")
    insertvalue('BTC',10000,'BUY','Sportbank', "C41")
    insertvalue('BUSD',10000,'BUY','Sportbank', "D41")
    insertvalue('BNB',10000,'BUY','Sportbank', "E41")
    insertvalue('ETH',10000,'BUY','Sportbank', "F41")
    insertvalue('UAH',10000,'BUY','Sportbank', "G41")
    insertvalue('SHIB',10000,'BUY','Sportbank', "H41")


    insertvalue('USDT',10000,'BUY','Izibank', "B42")
    insertvalue('BTC',10000,'BUY','Izibank', "C42")
    insertvalue('BUSD',10000,'BUY','Izibank', "D42")
    insertvalue('BNB',10000,'BUY','Izibank', "E42")
    insertvalue('ETH',10000,'BUY','Izibank', "F42")
    insertvalue('UAH',10000,'BUY','Izibank', "G42")
    insertvalue('SHIB',10000,'BUY','Izibank', "H42")     

    insertvalue('USDT',20000,'BUY','PrivatBank', "B50")
    insertvalue('BTC',20000,'BUY','PrivatBank', "C50")
    insertvalue('BUSD',20000,'BUY','PrivatBank', "D50")
    insertvalue('BNB',20000,'BUY','PrivatBank', "E50")
    insertvalue('ETH',20000,'BUY','PrivatBank', "F50")
    insertvalue('UAH',20000,'BUY','PrivatBank', "G50")
    insertvalue('SHIB',20000,'BUY','PrivatBank', "H50")

    insertvalue('USDT',20000,'BUY','Monobank', "B51")
    insertvalue('BTC',20000,'BUY','Monobank', "C51")
    insertvalue('BUSD',20000,'BUY','Monobank', "D51")
    insertvalue('BNB',20000,'BUY','Monobank', "E51")
    insertvalue('ETH',20000,'BUY','Monobank', "F51")
    insertvalue('UAH',20000,'BUY','Monobank', "G51")
    insertvalue('SHIB',20000,'BUY','Monobank', "H51")

    insertvalue('USDT',20000,'BUY','ABank', "B53")
    insertvalue('BTC',20000,'BUY','ABank', "C53")
    insertvalue('BUSD',20000,'BUY','ABank', "D53")
    insertvalue('BNB',20000,'BUY','ABank', "E53")
    insertvalue('ETH',20000,'BUY','ABank', "F53")
    insertvalue('UAH',20000,'BUY','ABank', "G53")
    insertvalue('SHIB',20000,'BUY','ABank', "H53")

    insertvalue('USDT',20000,'BUY','Pumbbank', "B54")
    insertvalue('BTC',20000,'BUY','Pumbbank', "C54")
    insertvalue('BUSD',20000,'BUY','Pumbbank', "D54")
    insertvalue('BNB',20000,'BUY','Pumbbank', "E54")
    insertvalue('ETH',20000,'BUY','Pumbbank', "F54")
    insertvalue('UAH',20000,'BUY','Pumbbank', "G54")
    insertvalue('SHIB',20000,'BUY','Pumbbank', "H54")

    insertvalue('USDT',20000,'BUY','Sportbank', "B55")
    insertvalue('BTC',20000,'BUY','Sportbank', "C55")
    insertvalue('BUSD',20000,'BUY','Sportbank', "D55")
    insertvalue('BNB',20000,'BUY','Sportbank', "E55")
    insertvalue('ETH',20000,'BUY','Sportbank', "F55")
    insertvalue('UAH',20000,'BUY','Sportbank', "G55")
    insertvalue('SHIB',20000,'BUY','Sportbank', "H55")


    insertvalue('USDT',20000,'BUY','Izibank', "B56")
    insertvalue('BTC',20000,'BUY','Izibank', "C56")
    insertvalue('BUSD',20000,'BUY','Izibank', "D56")
    insertvalue('BNB',20000,'BUY','Izibank', "E56")
    insertvalue('ETH',20000,'BUY','Izibank', "F56")
    insertvalue('UAH',20000,'BUY','Izibank', "G56")
    insertvalue('SHIB',20000,'BUY','Izibank', "H56") 


    insertvalue('USDT',50000,'BUY','PrivatBank', "B64")
    insertvalue('BTC',50000,'BUY','PrivatBank', "C64")
    insertvalue('BUSD',50000,'BUY','PrivatBank', "D64")
    insertvalue('BNB',50000,'BUY','PrivatBank', "E64")
    insertvalue('ETH',50000,'BUY','PrivatBank', "F64")
    insertvalue('UAH',50000,'BUY','PrivatBank', "G64")
    insertvalue('SHIB',50000,'BUY','PrivatBank', "H64")

    insertvalue('USDT',50000,'BUY','Monobank', "B65")
    insertvalue('BTC',50000,'BUY','Monobank', "C65")
    insertvalue('BUSD',50000,'BUY','Monobank', "D65")
    insertvalue('BNB',50000,'BUY','Monobank', "E65")
    insertvalue('ETH',50000,'BUY','Monobank', "F65")
    insertvalue('UAH',50000,'BUY','Monobank', "G65")
    insertvalue('SHIB',50000,'BUY','Monobank', "H65")

    insertvalue('USDT',50000,'BUY','ABank', "B67")
    insertvalue('BTC',50000,'BUY','ABank', "C67")
    insertvalue('BUSD',50000,'BUY','ABank', "D67")
    insertvalue('BNB',50000,'BUY','ABank', "E67")
    insertvalue('ETH',50000,'BUY','ABank', "F67")
    insertvalue('UAH',50000,'BUY','ABank', "G67")
    insertvalue('SHIB',50000,'BUY','ABank', "H67")

    insertvalue('USDT',50000,'BUY','Pumbbank', "B68")
    insertvalue('BTC',50000,'BUY','Pumbbank', "C68")
    insertvalue('BUSD',50000,'BUY','Pumbbank', "D68")
    insertvalue('BNB',50000,'BUY','Pumbbank', "E68")
    insertvalue('ETH',50000,'BUY','Pumbbank', "F68")
    insertvalue('UAH',50000,'BUY','Pumbbank', "G68")
    insertvalue('SHIB',50000,'BUY','Pumbbank', "H68")

    insertvalue('USDT',50000,'BUY','Sportbank', "B69")
    insertvalue('BTC',50000,'BUY','Sportbank', "C69")
    insertvalue('BUSD',50000,'BUY','Sportbank', "D69")
    insertvalue('BNB',50000,'BUY','Sportbank', "E69")
    insertvalue('ETH',50000,'BUY','Sportbank', "F69")
    insertvalue('UAH',50000,'BUY','Sportbank', "G69")
    insertvalue('SHIB',50000,'BUY','Sportbank', "H69")


    insertvalue('USDT',50000,'BUY','Izibank', "B70")
    insertvalue('BTC',50000,'BUY','Izibank', "C70")
    insertvalue('BUSD',50000,'BUY','Izibank', "D70")
    insertvalue('BNB',50000,'BUY','Izibank', "E70")
    insertvalue('ETH',50000,'BUY','Izibank', "F70")
    insertvalue('UAH',50000,'BUY','Izibank', "G70")
    insertvalue('SHIB',50000,'BUY','Izibank', "H70") 

    insertvalue('USDT',80000,'BUY','PrivatBank', "B78")
    insertvalue('BTC',80000,'BUY','PrivatBank', "C78")
    insertvalue('BUSD',80000,'BUY','PrivatBank', "D78")
    insertvalue('BNB',80000,'BUY','PrivatBank', "E78")
    insertvalue('ETH',80000,'BUY','PrivatBank', "F78")
    insertvalue('UAH',80000,'BUY','PrivatBank', "G78")
    insertvalue('SHIB',80000,'BUY','PrivatBank', "H78")

    insertvalue('USDT',80000,'BUY','Monobank', "B79")
    insertvalue('BTC',80000,'BUY','Monobank', "C79")
    insertvalue('BUSD',80000,'BUY','Monobank', "D79")
    insertvalue('BNB',80000,'BUY','Monobank', "E79")
    insertvalue('ETH',80000,'BUY','Monobank', "F79")
    insertvalue('UAH',80000,'BUY','Monobank', "G79")
    insertvalue('SHIB',80000,'BUY','Monobank', "H79")

    insertvalue('USDT',80000,'BUY','ABank', "B81")
    insertvalue('BTC',80000,'BUY','ABank', "C81")
    insertvalue('BUSD',80000,'BUY','ABank', "D81")
    insertvalue('BNB',80000,'BUY','ABank', "E81")
    insertvalue('ETH',80000,'BUY','ABank', "F81")
    insertvalue('UAH',80000,'BUY','ABank', "G81")
    insertvalue('SHIB',80000,'BUY','ABank', "H81")

    insertvalue('USDT',80000,'BUY','Pumbbank', "B82")
    insertvalue('BTC',80000,'BUY','Pumbbank', "C82")
    insertvalue('BUSD',80000,'BUY','Pumbbank', "D82")
    insertvalue('BNB',80000,'BUY','Pumbbank', "E82")
    insertvalue('ETH',80000,'BUY','Pumbbank', "F82")
    insertvalue('UAH',80000,'BUY','Pumbbank', "G82")
    insertvalue('SHIB',80000,'BUY','Pumbbank', "H82")

    insertvalue('USDT',80000,'BUY','Sportbank', "B83")
    insertvalue('BTC',80000,'BUY','Sportbank', "C83")
    insertvalue('BUSD',80000,'BUY','Sportbank', "D83")
    insertvalue('BNB',80000,'BUY','Sportbank', "E83")
    insertvalue('ETH',80000,'BUY','Sportbank', "F83")
    insertvalue('UAH',80000,'BUY','Sportbank', "G83")
    insertvalue('SHIB',80000,'BUY','Sportbank', "H83")


    insertvalue('USDT',80000,'BUY','Izibank', "B84")
    insertvalue('BTC',80000,'BUY','Izibank', "C84")
    insertvalue('BUSD',80000,'BUY','Izibank', "D84")
    insertvalue('BNB',80000,'BUY','Izibank', "E84")
    insertvalue('ETH',80000,'BUY','Izibank', "F84")
    insertvalue('UAH',80000,'BUY','Izibank', "G84")
    insertvalue('SHIB',80000,'BUY','Izibank', "H84") 


    insertvalue('USDT',100000,'BUY','PrivatBank', "B92")
    insertvalue('BTC',100000,'BUY','PrivatBank', "C92")
    insertvalue('BUSD',100000,'BUY','PrivatBank', "D92")
    insertvalue('BNB',100000,'BUY','PrivatBank', "E92")
    insertvalue('ETH',100000,'BUY','PrivatBank', "F92")
    insertvalue('UAH',100000,'BUY','PrivatBank', "G92")
    insertvalue('SHIB',100000,'BUY','PrivatBank', "H92")

    insertvalue('USDT',100000,'BUY','Monobank', "B93")
    insertvalue('BTC',100000,'BUY','Monobank', "C93")
    insertvalue('BUSD',100000,'BUY','Monobank', "D93")
    insertvalue('BNB',100000,'BUY','Monobank', "E93")
    insertvalue('ETH',100000,'BUY','Monobank', "F93")
    insertvalue('UAH',100000,'BUY','Monobank', "G93")
    insertvalue('SHIB',100000,'BUY','Monobank', "H93")

    insertvalue('USDT',100000,'BUY','ABank', "B95")
    insertvalue('BTC',100000,'BUY','ABank', "C95")
    insertvalue('BUSD',100000,'BUY','ABank', "D95")
    insertvalue('BNB',100000,'BUY','ABank', "E95")
    insertvalue('ETH',100000,'BUY','ABank', "F95")
    insertvalue('UAH',100000,'BUY','ABank', "G95")
    insertvalue('SHIB',100000,'BUY','ABank', "H95")

    insertvalue('USDT',100000,'BUY','Pumbbank', "B96")
    insertvalue('BTC',100000,'BUY','Pumbbank', "C96")
    insertvalue('BUSD',100000,'BUY','Pumbbank', "D96")
    insertvalue('BNB',100000,'BUY','Pumbbank', "E96")
    insertvalue('ETH',100000,'BUY','Pumbbank', "F96")
    insertvalue('UAH',100000,'BUY','Pumbbank', "G96")
    insertvalue('SHIB',100000,'BUY','Pumbbank', "H96")

    insertvalue('USDT',100000,'BUY','Sportbank', "B97")
    insertvalue('BTC',100000,'BUY','Sportbank', "C97")
    insertvalue('BUSD',100000,'BUY','Sportbank', "D97")
    insertvalue('BNB',100000,'BUY','Sportbank', "E97")
    insertvalue('ETH',100000,'BUY','Sportbank', "F97")
    insertvalue('UAH',100000,'BUY','Sportbank', "G97")
    insertvalue('SHIB',100000,'BUY','Sportbank', "H97")


    insertvalue('USDT',100000,'BUY','Izibank', "B98")
    insertvalue('BTC',100000,'BUY','Izibank', "C98")
    insertvalue('BUSD',100000,'BUY','Izibank', "D98")
    insertvalue('BNB',100000,'BUY','Izibank', "E98")
    insertvalue('ETH',100000,'BUY','Izibank', "F98")
    insertvalue('UAH',100000,'BUY','Izibank', "G98")
    insertvalue('SHIB',100000,'BUY','Izibank', "H98") 

    insertvalue('USDT',200000,'BUY','PrivatBank', "B106")
    insertvalue('BTC',200000,'BUY','PrivatBank', "C106")
    insertvalue('BUSD',200000,'BUY','PrivatBank', "D106")
    insertvalue('BNB',200000,'BUY','PrivatBank', "E106")
    insertvalue('ETH',200000,'BUY','PrivatBank', "F106")
    insertvalue('UAH',200000,'BUY','PrivatBank', "G106")
    insertvalue('SHIB',200000,'BUY','PrivatBank', "H106")

    insertvalue('USDT',200000,'BUY','Monobank', "B107")
    insertvalue('BTC',200000,'BUY','Monobank', "C107")
    insertvalue('BUSD',200000,'BUY','Monobank', "D107")
    insertvalue('BNB',200000,'BUY','Monobank', "E107")
    insertvalue('ETH',200000,'BUY','Monobank', "F107")
    insertvalue('UAH',200000,'BUY','Monobank', "G107")
    insertvalue('SHIB',200000,'BUY','Monobank', "H107")

    insertvalue('USDT',200000,'BUY','ABank', "B109")
    insertvalue('BTC',200000,'BUY','ABank', "C109")
    insertvalue('BUSD',200000,'BUY','ABank', "D109")
    insertvalue('BNB',200000,'BUY','ABank', "E109")
    insertvalue('ETH',200000,'BUY','ABank', "F109")
    insertvalue('UAH',200000,'BUY','ABank', "G109")
    insertvalue('SHIB',200000,'BUY','ABank', "H109")

    insertvalue('USDT',200000,'BUY','Pumbbank', "B110")
    insertvalue('BTC',200000,'BUY','Pumbbank', "C110")
    insertvalue('BUSD',200000,'BUY','Pumbbank', "D110")
    insertvalue('BNB',200000,'BUY','Pumbbank', "E110")
    insertvalue('ETH',200000,'BUY','Pumbbank', "F110")
    insertvalue('UAH',200000,'BUY','Pumbbank', "G110")
    insertvalue('SHIB',200000,'BUY','Pumbbank', "H110")

    insertvalue('USDT',200000,'BUY','Sportbank', "B111")
    insertvalue('BTC',200000,'BUY','Sportbank', "C111")
    insertvalue('BUSD',200000,'BUY','Sportbank', "D111")
    insertvalue('BNB',200000,'BUY','Sportbank', "E111")
    insertvalue('ETH',200000,'BUY','Sportbank', "F111")
    insertvalue('UAH',200000,'BUY','Sportbank', "G111")
    insertvalue('SHIB',200000,'BUY','Sportbank', "H111")


    insertvalue('USDT',200000,'BUY','Izibank', "B112")
    insertvalue('BTC',200000,'BUY','Izibank', "C112")
    insertvalue('BUSD',200000,'BUY','Izibank', "D112")
    insertvalue('BNB',200000,'BUY','Izibank', "E112")
    insertvalue('ETH',200000,'BUY','Izibank', "F112")
    insertvalue('UAH',200000,'BUY','Izibank', "G112")
    insertvalue('SHIB',200000,'BUY','Izibank', "H112") 
def SELLUAH():
    insertvalue1('USDT',0,'SELL','PrivatBank', "B8")
    insertvalue1('BTC',0,'SELL','PrivatBank', "C8")
    insertvalue1('BUSD',0,'SELL','PrivatBank', "D8")
    insertvalue1('BNB',0,'SELL','PrivatBank', "E8")
    insertvalue1('ETH',0,'SELL','PrivatBank', "F8")
    insertvalue1('UAH',0,'SELL','PrivatBank', "G8")
    insertvalue1('SHIB',0,'SELL','PrivatBank', "H8")

    insertvalue1('USDT',0,'SELL','Monobank', "B9")
    insertvalue1('BTC',0,'SELL','Monobank', "C9")
    insertvalue1('BUSD',0,'SELL','Monobank', "D9")
    insertvalue1('BNB',0,'SELL','Monobank', "E9")
    insertvalue1('ETH',0,'SELL','Monobank', "F9")
    insertvalue1('UAH',0,'SELL','Monobank', "G9")
    insertvalue1('SHIB',0,'SELL','Monobank', "H9")

    insertvalue1('USDT',0,'SELL','ABank', "B11")
    insertvalue1('BTC',0,'SELL','ABank', "C11")
    insertvalue1('BUSD',0,'SELL','ABank', "D11")
    insertvalue1('BNB',0,'SELL','ABank', "E11")
    insertvalue1('ETH',0,'SELL','ABank', "F11")
    insertvalue1('UAH',0,'SELL','ABank', "G11")
    insertvalue1('SHIB',0,'SELL','ABank', "H11")

    insertvalue1('USDT',0,'SELL','Pumbbank', "B12")
    insertvalue1('BTC',0,'SELL','Pumbbank', "C12")
    insertvalue1('BUSD',0,'SELL','Pumbbank', "D12")
    insertvalue1('BNB',0,'SELL','Pumbbank', "E12")
    insertvalue1('ETH',0,'SELL','Pumbbank', "F12")
    insertvalue1('UAH',0,'SELL','Pumbbank', "G12")
    insertvalue1('SHIB',0,'SELL','Pumbbank', "H12")

    insertvalue1('USDT',0,'SELL','Sportbank', "B13")
    insertvalue1('BTC',0,'SELL','Sportbank', "C13")
    insertvalue1('BUSD',0,'SELL','Sportbank', "D13")
    insertvalue1('BNB',0,'SELL','Sportbank', "E13")
    insertvalue1('ETH',0,'SELL','Sportbank', "F13")
    insertvalue1('UAH',0,'SELL','Sportbank', "G13")
    insertvalue1('SHIB',0,'SELL','Sportbank', "H13")


    insertvalue1('USDT',0,'SELL','Izibank', "B14")
    insertvalue1('BTC',0,'SELL','Izibank', "C14")
    insertvalue1('BUSD',0,'SELL','Izibank', "D14")
    insertvalue1('BNB',0,'SELL','Izibank', "E14")
    insertvalue1('ETH',0,'SELL','Izibank', "F14")
    insertvalue1('UAH',0,'SELL','Izibank', "G14")
    insertvalue1('SHIB',0,'SELL','Izibank', "H14")


    insertvalue1('USDT',1000,'SELL','PrivatBank', "B22")
    insertvalue1('BTC',1000,'SELL','PrivatBank', "C22")
    insertvalue1('BUSD',1000,'SELL','PrivatBank', "D22")
    insertvalue1('BNB',1000,'SELL','PrivatBank', "E22")
    insertvalue1('ETH',1000,'SELL','PrivatBank', "F22")
    insertvalue1('UAH',1000,'SELL','PrivatBank', "G22")
    insertvalue1('SHIB',1000,'SELL','PrivatBank', "H22")

    insertvalue1('USDT',1000,'SELL','Monobank', "B23")
    insertvalue1('BTC',1000,'SELL','Monobank', "C23")
    insertvalue1('BUSD',1000,'SELL','Monobank', "D23")
    insertvalue1('BNB',1000,'SELL','Monobank', "E23")
    insertvalue1('ETH',1000,'SELL','Monobank', "F23")
    insertvalue1('UAH',1000,'SELL','Monobank', "G23")
    insertvalue1('SHIB',1000,'SELL','Monobank', "H23")

    insertvalue1('USDT',1000,'SELL','ABank', "B25")
    insertvalue1('BTC',1000,'SELL','ABank', "C25")
    insertvalue1('BUSD',1000,'SELL','ABank', "D25")
    insertvalue1('BNB',1000,'SELL','ABank', "E25")
    insertvalue1('ETH',1000,'SELL','ABank', "F25")
    insertvalue1('UAH',1000,'SELL','ABank', "G25")
    insertvalue1('SHIB',1000,'SELL','ABank', "H25")

    insertvalue1('USDT',1000,'SELL','Pumbbank', "B26")
    insertvalue1('BTC',1000,'SELL','Pumbbank', "C26")
    insertvalue1('BUSD',1000,'SELL','Pumbbank', "D26")
    insertvalue1('BNB',1000,'SELL','Pumbbank', "E26")
    insertvalue1('ETH',1000,'SELL','Pumbbank', "F26")
    insertvalue1('UAH',1000,'SELL','Pumbbank', "G26")
    insertvalue1('SHIB',1000,'SELL','Pumbbank', "H26")

    insertvalue1('USDT',1000,'SELL','Sportbank', "B27")
    insertvalue1('BTC',1000,'SELL','Sportbank', "C27")
    insertvalue1('BUSD',1000,'SELL','Sportbank', "D27")
    insertvalue1('BNB',1000,'SELL','Sportbank', "E27")
    insertvalue1('ETH',1000,'SELL','Sportbank', "F27")
    insertvalue1('UAH',1000,'SELL','Sportbank', "G27")
    insertvalue1('SHIB',1000,'SELL','Sportbank', "H27")


    insertvalue1('USDT',1000,'SELL','Izibank', "B28")
    insertvalue1('BTC',1000,'SELL','Izibank', "C28")
    insertvalue1('BUSD',1000,'SELL','Izibank', "D28")
    insertvalue1('BNB',1000,'SELL','Izibank', "E28")
    insertvalue1('ETH',1000,'SELL','Izibank', "F28")
    insertvalue1('UAH',1000,'SELL','Izibank', "G28")
    insertvalue1('SHIB',1000,'SELL','Izibank', "H28")


    insertvalue1('USDT',10000,'SELL','PrivatBank', "B36")
    insertvalue1('BTC',10000,'SELL','PrivatBank', "C36")
    insertvalue1('BUSD',10000,'SELL','PrivatBank', "D36")
    insertvalue1('BNB',10000,'SELL','PrivatBank', "E36")
    insertvalue1('ETH',10000,'SELL','PrivatBank', "F36")
    insertvalue1('UAH',10000,'SELL','PrivatBank', "G36")
    insertvalue1('SHIB',10000,'SELL','PrivatBank', "H36")

    insertvalue1('USDT',10000,'SELL','Monobank', "B37")
    insertvalue1('BTC',10000,'SELL','Monobank', "C37")
    insertvalue1('BUSD',10000,'SELL','Monobank', "D37")
    insertvalue1('BNB',10000,'SELL','Monobank', "E37")
    insertvalue1('ETH',10000,'SELL','Monobank', "F37")
    insertvalue1('UAH',10000,'SELL','Monobank', "G37")
    insertvalue1('SHIB',10000,'SELL','Monobank', "H37")

    insertvalue1('USDT',10000,'SELL','ABank', "B39")
    insertvalue1('BTC',10000,'SELL','ABank', "C39")
    insertvalue1('BUSD',10000,'SELL','ABank', "D39")
    insertvalue1('BNB',10000,'SELL','ABank', "E39")
    insertvalue1('ETH',10000,'SELL','ABank', "F39")
    insertvalue1('UAH',10000,'SELL','ABank', "G39")
    insertvalue1('SHIB',10000,'SELL','ABank', "H39")

    insertvalue1('USDT',10000,'SELL','Pumbbank', "B40")
    insertvalue1('BTC',10000,'SELL','Pumbbank', "C40")
    insertvalue1('BUSD',10000,'SELL','Pumbbank', "D40")
    insertvalue1('BNB',10000,'SELL','Pumbbank', "E40")
    insertvalue1('ETH',10000,'SELL','Pumbbank', "F40")
    insertvalue1('UAH',10000,'SELL','Pumbbank', "G40")
    insertvalue1('SHIB',10000,'SELL','Pumbbank', "H40")

    insertvalue1('USDT',10000,'SELL','Sportbank', "B41")
    insertvalue1('BTC',10000,'SELL','Sportbank', "C41")
    insertvalue1('BUSD',10000,'SELL','Sportbank', "D41")
    insertvalue1('BNB',10000,'SELL','Sportbank', "E41")
    insertvalue1('ETH',10000,'SELL','Sportbank', "F41")
    insertvalue1('UAH',10000,'SELL','Sportbank', "G41")
    insertvalue1('SHIB',10000,'SELL','Sportbank', "H41")


    insertvalue1('USDT',10000,'SELL','Izibank', "B42")
    insertvalue1('BTC',10000,'SELL','Izibank', "C42")
    insertvalue1('BUSD',10000,'SELL','Izibank', "D42")
    insertvalue1('BNB',10000,'SELL','Izibank', "E42")
    insertvalue1('ETH',10000,'SELL','Izibank', "F42")
    insertvalue1('UAH',10000,'SELL','Izibank', "G42")
    insertvalue1('SHIB',10000,'SELL','Izibank', "H42")     

    insertvalue1('USDT',20000,'SELL','PrivatBank', "B50")
    insertvalue1('BTC',20000,'SELL','PrivatBank', "C50")
    insertvalue1('BUSD',20000,'SELL','PrivatBank', "D50")
    insertvalue1('BNB',20000,'SELL','PrivatBank', "E50")
    insertvalue1('ETH',20000,'SELL','PrivatBank', "F50")
    insertvalue1('UAH',20000,'SELL','PrivatBank', "G50")
    insertvalue1('SHIB',20000,'SELL','PrivatBank', "H50")

    insertvalue1('USDT',20000,'SELL','Monobank', "B51")
    insertvalue1('BTC',20000,'SELL','Monobank', "C51")
    insertvalue1('BUSD',20000,'SELL','Monobank', "D51")
    insertvalue1('BNB',20000,'SELL','Monobank', "E51")
    insertvalue1('ETH',20000,'SELL','Monobank', "F51")
    insertvalue1('UAH',20000,'SELL','Monobank', "G51")
    insertvalue1('SHIB',20000,'SELL','Monobank', "H51")

    insertvalue1('USDT',20000,'SELL','ABank', "B53")
    insertvalue1('BTC',20000,'SELL','ABank', "C53")
    insertvalue1('BUSD',20000,'SELL','ABank', "D53")
    insertvalue1('BNB',20000,'SELL','ABank', "E53")
    insertvalue1('ETH',20000,'SELL','ABank', "F53")
    insertvalue1('UAH',20000,'SELL','ABank', "G53")
    insertvalue1('SHIB',20000,'SELL','ABank', "H53")

    insertvalue1('USDT',20000,'SELL','Pumbbank', "B54")
    insertvalue1('BTC',20000,'SELL','Pumbbank', "C54")
    insertvalue1('BUSD',20000,'SELL','Pumbbank', "D54")
    insertvalue1('BNB',20000,'SELL','Pumbbank', "E54")
    insertvalue1('ETH',20000,'SELL','Pumbbank', "F54")
    insertvalue1('UAH',20000,'SELL','Pumbbank', "G54")
    insertvalue1('SHIB',20000,'SELL','Pumbbank', "H54")

    insertvalue1('USDT',20000,'SELL','Sportbank', "B55")
    insertvalue1('BTC',20000,'SELL','Sportbank', "C55")
    insertvalue1('BUSD',20000,'SELL','Sportbank', "D55")
    insertvalue1('BNB',20000,'SELL','Sportbank', "E55")
    insertvalue1('ETH',20000,'SELL','Sportbank', "F55")
    insertvalue1('UAH',20000,'SELL','Sportbank', "G55")
    insertvalue1('SHIB',20000,'SELL','Sportbank', "H55")


    insertvalue1('USDT',20000,'SELL','Izibank', "B56")
    insertvalue1('BTC',20000,'SELL','Izibank', "C56")
    insertvalue1('BUSD',20000,'SELL','Izibank', "D56")
    insertvalue1('BNB',20000,'SELL','Izibank', "E56")
    insertvalue1('ETH',20000,'SELL','Izibank', "F56")
    insertvalue1('UAH',20000,'SELL','Izibank', "G56")
    insertvalue1('SHIB',20000,'SELL','Izibank', "H56") 


    insertvalue1('USDT',50000,'SELL','PrivatBank', "B64")
    insertvalue1('BTC',50000,'SELL','PrivatBank', "C64")
    insertvalue1('BUSD',50000,'SELL','PrivatBank', "D64")
    insertvalue1('BNB',50000,'SELL','PrivatBank', "E64")
    insertvalue1('ETH',50000,'SELL','PrivatBank', "F64")
    insertvalue1('UAH',50000,'SELL','PrivatBank', "G64")
    insertvalue1('SHIB',50000,'SELL','PrivatBank', "H64")

    insertvalue1('USDT',50000,'SELL','Monobank', "B65")
    insertvalue1('BTC',50000,'SELL','Monobank', "C65")
    insertvalue1('BUSD',50000,'SELL','Monobank', "D65")
    insertvalue1('BNB',50000,'SELL','Monobank', "E65")
    insertvalue1('ETH',50000,'SELL','Monobank', "F65")
    insertvalue1('UAH',50000,'SELL','Monobank', "G65")
    insertvalue1('SHIB',50000,'SELL','Monobank', "H65")

    insertvalue1('USDT',50000,'SELL','ABank', "B67")
    insertvalue1('BTC',50000,'SELL','ABank', "C67")
    insertvalue1('BUSD',50000,'SELL','ABank', "D67")
    insertvalue1('BNB',50000,'SELL','ABank', "E67")
    insertvalue1('ETH',50000,'SELL','ABank', "F67")
    insertvalue1('UAH',50000,'SELL','ABank', "G67")
    insertvalue1('SHIB',50000,'SELL','ABank', "H67")

    insertvalue1('USDT',50000,'SELL','Pumbbank', "B68")
    insertvalue1('BTC',50000,'SELL','Pumbbank', "C68")
    insertvalue1('BUSD',50000,'SELL','Pumbbank', "D68")
    insertvalue1('BNB',50000,'SELL','Pumbbank', "E68")
    insertvalue1('ETH',50000,'SELL','Pumbbank', "F68")
    insertvalue1('UAH',50000,'SELL','Pumbbank', "G68")
    insertvalue1('SHIB',50000,'SELL','Pumbbank', "H68")

    insertvalue1('USDT',50000,'SELL','Sportbank', "B69")
    insertvalue1('BTC',50000,'SELL','Sportbank', "C69")
    insertvalue1('BUSD',50000,'SELL','Sportbank', "D69")
    insertvalue1('BNB',50000,'SELL','Sportbank', "E69")
    insertvalue1('ETH',50000,'SELL','Sportbank', "F69")
    insertvalue1('UAH',50000,'SELL','Sportbank', "G69")
    insertvalue1('SHIB',50000,'SELL','Sportbank', "H69")


    insertvalue1('USDT',50000,'SELL','Izibank', "B70")
    insertvalue1('BTC',50000,'SELL','Izibank', "C70")
    insertvalue1('BUSD',50000,'SELL','Izibank', "D70")
    insertvalue1('BNB',50000,'SELL','Izibank', "E70")
    insertvalue1('ETH',50000,'SELL','Izibank', "F70")
    insertvalue1('UAH',50000,'SELL','Izibank', "G70")
    insertvalue1('SHIB',50000,'SELL','Izibank', "H70") 

    insertvalue1('USDT',80000,'SELL','PrivatBank', "B78")
    insertvalue1('BTC',80000,'SELL','PrivatBank', "C78")
    insertvalue1('BUSD',80000,'SELL','PrivatBank', "D78")
    insertvalue1('BNB',80000,'SELL','PrivatBank', "E78")
    insertvalue1('ETH',80000,'SELL','PrivatBank', "F78")
    insertvalue1('UAH',80000,'SELL','PrivatBank', "G78")
    insertvalue1('SHIB',80000,'SELL','PrivatBank', "H78")

    insertvalue1('USDT',80000,'SELL','Monobank', "B79")
    insertvalue1('BTC',80000,'SELL','Monobank', "C79")
    insertvalue1('BUSD',80000,'SELL','Monobank', "D79")
    insertvalue1('BNB',80000,'SELL','Monobank', "E79")
    insertvalue1('ETH',80000,'SELL','Monobank', "F79")
    insertvalue1('UAH',80000,'SELL','Monobank', "G79")
    insertvalue1('SHIB',80000,'SELL','Monobank', "H79")

    insertvalue1('USDT',80000,'SELL','ABank', "B81")
    insertvalue1('BTC',80000,'SELL','ABank', "C81")
    insertvalue1('BUSD',80000,'SELL','ABank', "D81")
    insertvalue1('BNB',80000,'SELL','ABank', "E81")
    insertvalue1('ETH',80000,'SELL','ABank', "F81")
    insertvalue1('UAH',80000,'SELL','ABank', "G81")
    insertvalue1('SHIB',80000,'SELL','ABank', "H81")

    insertvalue1('USDT',80000,'SELL','Pumbbank', "B82")
    insertvalue1('BTC',80000,'SELL','Pumbbank', "C82")
    insertvalue1('BUSD',80000,'SELL','Pumbbank', "D82")
    insertvalue1('BNB',80000,'SELL','Pumbbank', "E82")
    insertvalue1('ETH',80000,'SELL','Pumbbank', "F82")
    insertvalue1('UAH',80000,'SELL','Pumbbank', "G82")
    insertvalue1('SHIB',80000,'SELL','Pumbbank', "H82")

    insertvalue1('USDT',80000,'SELL','Sportbank', "B83")
    insertvalue1('BTC',80000,'SELL','Sportbank', "C83")
    insertvalue1('BUSD',80000,'SELL','Sportbank', "D83")
    insertvalue1('BNB',80000,'SELL','Sportbank', "E83")
    insertvalue1('ETH',80000,'SELL','Sportbank', "F83")
    insertvalue1('UAH',80000,'SELL','Sportbank', "G83")
    insertvalue1('SHIB',80000,'SELL','Sportbank', "H83")


    insertvalue1('USDT',80000,'SELL','Izibank', "B84")
    insertvalue1('BTC',80000,'SELL','Izibank', "C84")
    insertvalue1('BUSD',80000,'SELL','Izibank', "D84")
    insertvalue1('BNB',80000,'SELL','Izibank', "E84")
    insertvalue1('ETH',80000,'SELL','Izibank', "F84")
    insertvalue1('UAH',80000,'SELL','Izibank', "G84")
    insertvalue1('SHIB',80000,'SELL','Izibank', "H84") 


    insertvalue1('USDT',100000,'SELL','PrivatBank', "B92")
    insertvalue1('BTC',100000,'SELL','PrivatBank', "C92")
    insertvalue1('BUSD',100000,'SELL','PrivatBank', "D92")
    insertvalue1('BNB',100000,'SELL','PrivatBank', "E92")
    insertvalue1('ETH',100000,'SELL','PrivatBank', "F92")
    insertvalue1('UAH',100000,'SELL','PrivatBank', "G92")
    insertvalue1('SHIB',100000,'SELL','PrivatBank', "H92")

    insertvalue1('USDT',100000,'SELL','Monobank', "B93")
    insertvalue1('BTC',100000,'SELL','Monobank', "C93")
    insertvalue1('BUSD',100000,'SELL','Monobank', "D93")
    insertvalue1('BNB',100000,'SELL','Monobank', "E93")
    insertvalue1('ETH',100000,'SELL','Monobank', "F93")
    insertvalue1('UAH',100000,'SELL','Monobank', "G93")
    insertvalue1('SHIB',100000,'SELL','Monobank', "H93")

    insertvalue1('USDT',100000,'SELL','ABank', "B95")
    insertvalue1('BTC',100000,'SELL','ABank', "C95")
    insertvalue1('BUSD',100000,'SELL','ABank', "D95")
    insertvalue1('BNB',100000,'SELL','ABank', "E95")
    insertvalue1('ETH',100000,'SELL','ABank', "F95")
    insertvalue1('UAH',100000,'SELL','ABank', "G95")
    insertvalue1('SHIB',100000,'SELL','ABank', "H95")

    insertvalue1('USDT',100000,'SELL','Pumbbank', "B96")
    insertvalue1('BTC',100000,'SELL','Pumbbank', "C96")
    insertvalue1('BUSD',100000,'SELL','Pumbbank', "D96")
    insertvalue1('BNB',100000,'SELL','Pumbbank', "E96")
    insertvalue1('ETH',100000,'SELL','Pumbbank', "F96")
    insertvalue1('UAH',100000,'SELL','Pumbbank', "G96")
    insertvalue1('SHIB',100000,'SELL','Pumbbank', "H96")

    insertvalue1('USDT',100000,'SELL','Sportbank', "B97")
    insertvalue1('BTC',100000,'SELL','Sportbank', "C97")
    insertvalue1('BUSD',100000,'SELL','Sportbank', "D97")
    insertvalue1('BNB',100000,'SELL','Sportbank', "E97")
    insertvalue1('ETH',100000,'SELL','Sportbank', "F97")
    insertvalue1('UAH',100000,'SELL','Sportbank', "G97")
    insertvalue1('SHIB',100000,'SELL','Sportbank', "H97")


    insertvalue1('USDT',100000,'SELL','Izibank', "B98")
    insertvalue1('BTC',100000,'SELL','Izibank', "C98")
    insertvalue1('BUSD',100000,'SELL','Izibank', "D98")
    insertvalue1('BNB',100000,'SELL','Izibank', "E98")
    insertvalue1('ETH',100000,'SELL','Izibank', "F98")
    insertvalue1('UAH',100000,'SELL','Izibank', "G98")
    insertvalue1('SHIB',100000,'SELL','Izibank', "H98") 

    insertvalue1('USDT',200000,'SELL','PrivatBank', "B106")
    insertvalue1('BTC',200000,'SELL','PrivatBank', "C106")
    insertvalue1('BUSD',200000,'SELL','PrivatBank', "D106")
    insertvalue1('BNB',200000,'SELL','PrivatBank', "E106")
    insertvalue1('ETH',200000,'SELL','PrivatBank', "F106")
    insertvalue1('UAH',200000,'SELL','PrivatBank', "G106")
    insertvalue1('SHIB',200000,'SELL','PrivatBank', "H106")

    insertvalue1('USDT',200000,'SELL','Monobank', "B107")
    insertvalue1('BTC',200000,'SELL','Monobank', "C107")
    insertvalue1('BUSD',200000,'SELL','Monobank', "D107")
    insertvalue1('BNB',200000,'SELL','Monobank', "E107")
    insertvalue1('ETH',200000,'SELL','Monobank', "F107")
    insertvalue1('UAH',200000,'SELL','Monobank', "G107")
    insertvalue1('SHIB',200000,'SELL','Monobank', "H107")

    insertvalue1('USDT',200000,'SELL','ABank', "B109")
    insertvalue1('BTC',200000,'SELL','ABank', "C109")
    insertvalue1('BUSD',200000,'SELL','ABank', "D109")
    insertvalue1('BNB',200000,'SELL','ABank', "E109")
    insertvalue1('ETH',200000,'SELL','ABank', "F109")
    insertvalue1('UAH',200000,'SELL','ABank', "G109")
    insertvalue1('SHIB',200000,'SELL','ABank', "H109")

    insertvalue1('USDT',200000,'SELL','Pumbbank', "B110")
    insertvalue1('BTC',200000,'SELL','Pumbbank', "C110")
    insertvalue1('BUSD',200000,'SELL','Pumbbank', "D110")
    insertvalue1('BNB',200000,'SELL','Pumbbank', "E110")
    insertvalue1('ETH',200000,'SELL','Pumbbank', "F110")
    insertvalue1('UAH',200000,'SELL','Pumbbank', "G110")
    insertvalue1('SHIB',200000,'SELL','Pumbbank', "H110")

    insertvalue1('USDT',200000,'SELL','Sportbank', "B111")
    insertvalue1('BTC',200000,'SELL','Sportbank', "C111")
    insertvalue1('BUSD',200000,'SELL','Sportbank', "D111")
    insertvalue1('BNB',200000,'SELL','Sportbank', "E111")
    insertvalue1('ETH',200000,'SELL','Sportbank', "F111")
    insertvalue1('UAH',200000,'SELL','Sportbank', "G111")
    insertvalue1('SHIB',200000,'SELL','Sportbank', "H111")


    insertvalue1('USDT',200000,'SELL','Izibank', "B112")
    insertvalue1('BTC',200000,'SELL','Izibank', "C112")
    insertvalue1('BUSD',200000,'SELL','Izibank', "D112")
    insertvalue1('BNB',200000,'SELL','Izibank', "E112")
    insertvalue1('ETH',200000,'SELL','Izibank', "F112")
    insertvalue1('UAH',200000,'SELL','Izibank', "G112")
    insertvalue1('SHIB',200000,'SELL','Izibank', "H112")

BUYUAH()
SELLUAH()
getMarketPrice()
