# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

#number_of_students = len(student_heights)
number_of_students = 0
total_height = 0
avg_height = 0

for student in student_heights:
  number_of_students += 1
  total_height += student

print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")

avg_height = int (round(total_height/number_of_students))
print(f"average height = {avg_height}")

