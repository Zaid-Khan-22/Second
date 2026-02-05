def sum_of_tuples(lst):
    result = []
    for a, b in lst:
        result.append(a + b)
    return result

input_data = [(1, 2), (3, 4), (5, 6)]
print(sum_of_tuples(input_data))
