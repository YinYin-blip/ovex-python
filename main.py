import csv
from ovex import *

def main():
    orderbook = getOrderBookOvex()
    for ask in orderbook['asks']:
        print(ask)

if __name__ == "__main__":
    main()
