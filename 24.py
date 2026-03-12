from functools import reduce

def totalRevenue(cust):
    return reduce(
        lambda total, purchase: total + purchase + purchase/10
        if isValid(purchase, cust["active"])
        else total,
        cust["purchases"],
        0
    )

def isValid(price, active):
    return price > 100 and active

customers = [
    {"name": "A", "purchases": [50, 200, 300], "active": True},
    {"name": "B", "purchases": [500, 20], "active": False},
    {"name": "C", "purchases": [150, 250], "active": True}
]

total = reduce(lambda acc, cust: acc + totalRevenue(cust), customers, 0)

print(total)
