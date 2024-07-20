height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi=float(weight / (height ** 2))
bmi_format=bmi
#bmi_format="{:.5f}".format(bmi)
#print(f"(BMI - {bmi}")

if bmi < 18.5:
  print(f"Your BMI is {bmi_format}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi_format}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi_format}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi_format}, you are obese.")
else:
  print(f"Your BMI is {bmi_format}, you are clinically obese.")


