inpt = ['flower', 'flow', 'flight']
pre = ""
for i in range(len(inpt[0])):
    t = inpt[0][:i+1]
    there = True
    for word in inpt:
        if not word.startswith(t):
            there = False
            break
    if there:
        pre = t
    else:
        break
print(pre)