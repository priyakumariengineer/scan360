import time
from binance.client import Client 
from binance.websockets import BinanceSocketManager 

API = "LQ56bLtL6O1CcmXqgO2pQpFrYcT7AyeU99BJCs1wa1HMhFVpaT9Et2F34xJ3NWwf"
SECRET = "Ew2BxAKhfjAhN8NkPEhoWrvtSP9NNx15X8gYcJ22efYFxM2MxzCKDbtfrTeuPbUw"


client = Client(api_key=API, api_secret=SECRET)


bm = BinanceSocketManager(client)

def processmessage(msg):
    print(msg['p'])

conn_key = bm.start_trade_socket('ETHBTC', processmessage)

bm.start()

# let some data flow..
time.sleep(10)

# stop the socket manager
bm.stop_socket(conn_key)


