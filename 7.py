str = input("Enter word without space:")
v = ['A','E','I','O','U','a','e','i','o','u']
vowels = []
consonants = []
for c in str:
    if c in v:
        vowels.append(c)
    else:
        consonants.append(c)
print("Vowels:\n",vowels)
print("Consonants:\n",consonants)