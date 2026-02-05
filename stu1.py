students = {}
for i in range(5):
    r = input("Enter the student roll no.")
    n = input("Enter the student name")
    m = input("Enter the student marks")
    students.update({r:(n,m)})
print(students)