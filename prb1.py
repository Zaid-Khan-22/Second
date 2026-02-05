# take a variable attendance and intialize it with a string tht contains a number print the exam elgibility of a candidate if attendance is greater than equal to 75
attendance = input("Enter your attendance")
a = int(attendance)
if(a>=75):
    print("Eligible for examination")
else :
    print("Low attendance")

#list to set 
l = [1,2,3,4,5,3,2,4]
s = set(l)
print(s)

#dict using zip
d = {"name":"abc","roll no": 2 ,"age":18}
key = ["name","roll no","age"]
val = ["abc",2,18]
dict = zip(key,val)
print(d)