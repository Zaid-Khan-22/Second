while True:
    b = input("Enter X to exit: ")
    if b.lower() == "x":
        break
    else:
        x = int(input("Enter a number: "))
        n = int(input("Enter the number of characters: "))
        for i in range(0,n):
            for j in range(0,i+1):
                print(" ",x,end="")
            print("\n")