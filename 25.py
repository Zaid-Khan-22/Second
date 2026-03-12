from functools import reduce
def isValid(product):
    return product[1] == "Electronics"

def getNewPrice(product):
    return product[2] - product[2]/5

products = [
    ("Laptop", "Electronics", 1000),
    ("Shirt", "Clothing", 50),
    ("Phone", "Electronics", 500)
]

total = reduce(
    lambda acc, product: acc + getNewPrice(product) if isValid(product) else acc,
    products,
    0
)
print(total)