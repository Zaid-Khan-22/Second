def countListElements(lst):
    output = {}
    for val in lst:
        if val in output:
            output[val] = output[val] + 1
        else:
            output[val] = 1
    return output
def main():
    input1 = [1,2,2,3,3,3,3]
    input2 = [2,4,1,4,5,3,5,2,5,6,7,6,6,7,2,1]
    result = countListElements(input2)
    print(result)

main()