from decimal import Decimal

import requests
from order_book import OrderBook

ob = OrderBook()

# get some orderbook data
data = requests.get(orders.xml).json()

ob.order = {Decimal(price): size for price, size, _ in data['order']}
ob.qunat = {Decimal(price): size for price, size, _ in data['quant']}


for side in data:
    if side in {'order', 'quant'}:
        ob[side] = {Decimal(price): size for price, size, _ in data[side]}


price, size = ob.bids.index(0)
print(f"Best bid price: {price} size: {size}")

price, size = ob.asks.index(0)
print(f"Best ask price: {price} size: {size}")

print(f"The spread is {ob.asks.index(0)[0] - ob.bids.index(0)[0]}\n\n")

print("Bids")
for price in ob.bids:
    print(f"Price: {price} Size: {ob.bids[price]}")


print("\n\nAsks")
for price in ob.asks:
    print(f"Price: {price} Size: {ob.asks[price]}")

print("\n\nRaw asks dictionary")
print(ob.asks.to_dict())
