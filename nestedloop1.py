# Program to calculate BMI (height in cm)

weight = float(input("Enter your weight in kilograms: "))
height_cm = float(input("Enter your height in centimeters: "))

# Convert height from cm to meters
height_m = height_cm / 100

bmi = weight / (height_m ** 2)

print("Your BMI is:", round(bmi, 2))

# BMI Category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
