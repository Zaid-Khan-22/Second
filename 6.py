odd = []
even = []
for i in range(3):
    num = int(input("Enter number:"))
    if(num %2 == 0):
        even.append(num)
    else:
        odd.append(num)
print("Odd:\n",odd)
print("Even:\n",even)