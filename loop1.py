for i in range(1,50,1):
    if(i%3 == 0 and  i%5 == 0):
        print("Fizz & Buzz")
    elif(i%3 == 0):
        print("Buzz")
    elif(i%5 == 0):
        print("Buzz")
    else:
        print(i)


num = int(input("Enter number"))
sum = 0

while num>0:
    r = num%10
    sum += r
    num = num //10
print("The sum of digits is",sum)


