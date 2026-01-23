def e_o(num):
    if num%2 == 0:
        print("Even")
    else:
        print("Odd")

def inp():
    return int(input("Enter number\n"))

num = inp()
e_o(num)