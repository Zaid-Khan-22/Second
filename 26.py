from functools import reduce
students = [
    {"name": "A", "marks": [50, 60, 70]},
    {"name": "B", "marks": [30, 40]},
    {"name": "C", "marks": [80, 90]}
]
def isValid(student):
    marks = student["marks"]
    return sum(marks) / len(marks) >= 60

total = reduce(
    lambda acc, student:
        acc + sum(mark + 5 for mark in student["marks"])
        if isValid(student) else acc,
    students,
    0
)

print(total)