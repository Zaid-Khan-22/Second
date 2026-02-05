num = [3,2,6,4,8,5]
sum = []
for i in range(len(num)):
    n = 0
    for j in range(i+1):
        n += num[j]
    sum.append(n)
print("Sum:",sum)