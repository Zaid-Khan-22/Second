def unique_characters(s):
    seen = set()
    result = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return tuple(result)

text = "programming"
print(unique_characters(text))
