unit = int(input("Enter the number of units consumed"))
bill = 0
if(unit<=100):
    bill = unit
elif(unit > 100 and unit <= 200):
    bill = 100 + (unit - 100)*2
else:
    bill = 300 + (unit - 200)*3
print(f"Your bill:{bill}")