# ovex-python
Python SDK for Ovex API

## Installation
```git clone https://github.com/YinYin-blip/ovex-python```

## Usage
Update the auth.py file to include you Ovex API key


Example usage:
```from ovex import *
orderbook = getOrderBookOvex()
for ask in orderbook['asks']:
     print(ask)
```

Example output:
>{'market': 'btczar', 'executed_volume': '0.0', 'state': 'wait', 'price': '124965.0', 'remaining_volume': '0.019558', 'volume': '0.019558', 'side': 'sell', 'created_at': '2020-03-31T07:20:04+02:00', 'avg_price': '0.0', 'trades_count': 0, 'id': 53408891, 'ord_type': 'limit'}
