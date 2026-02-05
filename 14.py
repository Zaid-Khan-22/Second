def string_length_map(lst):
    result = {}
    for s in lst:
        result[s] = len(s)
    return result

input_data = ["python", "ml", "ai"]
print(string_length_map(input_data))
