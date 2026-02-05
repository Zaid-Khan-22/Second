def reverse_words(s):
    words = s.split()
    return words[::-1]

text = "data science is fun"
result = reverse_words(text)
print(result)
