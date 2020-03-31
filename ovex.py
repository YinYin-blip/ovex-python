import requests
import json
from auth import token

def apiRequest(request, payload=None, method="get", headers=None):

    base_url = "https://www.ovex.io/api/v2/"
    url = base_url + request

    if method == 'get':
        r = requests.get(url, params=payload, headers=headers)
    elif method=='post':
        r = requests.post(url, data=payload, headers=headers)

    if ((r.status_code/100) == 2):
        try:
            r = r.json()
        except ValueError:
            r = {'error': 'unable to parse as JSON'}
    return r

def getOrderBookOvex(market='btczar', asks_limit=None, bids_limit=None):
    request = 'order_book'
    payload = {
        'market': market,
        'asks_limit' : asks_limit,
        'bids_limit' : bids_limit
    }
    return apiRequest(request, payload)

def getHighestBidOvex(bids):
    bid = json['bids'][0]
    return bid

def getLowestAskOvex(asks):
    ask = json['asks'][0]
    return ask

def getOrderListOvex(market="btczar", state='wait', limit=100, page=1, order_by='asc'):
    request = 'orders'
    payload = {
        'market' : market,
        'state' : state,
        'limit' : limit,
        'page' : page,
        'order_by' : order_by
    }
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': "Bearer " + token()
    }
    return apiRequest(request, payload, 'get', headers)

def getAllOrderIDs():
    idList = []
    response = getOrderListOvex()
    if 'error' in response:
        #unable to continue executing because a non-json object was returned
        raise TypeError
    for order in response:
        idList.append(order['id'])
    return idList

def createOrderOvex(volume, price, side, market='btczar', order_type='limit'):#side, volume, price, order_type='limit', market='btczar'
    '''
    Param :volume: float, the amount of base currency
    Param :price: float, the value per one unit of base currency
    param :side: start, side of the order book - either 'sell' or 'buy'
    param :market: str (optional), currenct pair to trade (default 'btczar')
    param :order_type: str (optional), order type - either 'limit' or 'market' (default 'limit')
    '''#volume restriction on ovex is as low as 0.000001
    request = 'orders'
    payload = {
        'market': market,
        'side': side,
        'volume': volume,
        'price': price,
        'ord_type': order_type
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer ' + token()
    }

    return apiRequest(request, payload, "post", headers)

def deleteOrderOvex(orderID):
    request = "order/delete"

    payload = "id="+orderID
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': "Bearer " + token()
    }

    return apiRequest(request, payload, "post", headers)

def deleteAllOrdersOvex(idList):
    for orderID in idList:
        st = "Are you sure you want to delete order ID", orderID, "? [Y/N]"
        q = input(st)
        if q == 'Y':
            deleteOrderOvex(str(orderID))
        else:
            continue

def getFeesOvex(is_ask, pair='btczar'):
    request = "fees/trading"
    response = apiRequest(request, False)

    if 'error' in response:
        #unable to continue executing because a non-json object was returned
        raise TypeError

    for market in response:
        if market['market'] == pair:
            if is_ask:
                return float(market['ask_fee']['value'])
            elif not is_ask:
                return float(market['bid_fee']['value'])

def getAccountsOvex():
    request = "accounts"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': "Bearer " + token()
    }
    return apiRequest(request, None, 'get', headers)

def getAccountBalanceOvex():
    response = getAccountsOvex()
    return response
