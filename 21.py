def convertToDollar(item):
    return item[1] * 83

products = [
    ("Pen", 10),
    ("Bag", 50),
    ("Shoes", 60)
]

def isValid(price):
    return price > 3000

prices = list(map(convertToDollar, products))
print(prices)
print(list(filter(isValid, prices)))
