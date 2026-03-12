def editWord(word):
    return word.lower().strip()

def isValid(word):
    return len(word) > 5
words = ["  Python ", " AI ", "Machine ", " Data "]
newWords = list(map(editWord,words))
print(list(filter(isValid,newWords)))