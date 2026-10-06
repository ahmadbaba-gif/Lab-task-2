# Question #01:
print("=== Question 1 ===")
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours <= 40:
    total_pay = hours * rate
else:
    overtime_hours = hours - 40
    total_pay = (40 * rate) + (overtime_hours * rate * 1.5)

print("Total pay:", total_pay)








# Question #02;
print("\n=== Question 2 ===")
student_name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

marks = []
for i in range(5):
    m = float(input(f"Enter marks for subject {i + 1} (out of 100): "))
    marks.append(m)

total = sum(marks)
percentage = (total / 500) * 100

if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Fail if any subject is below 40
failed = False
for m in marks:
    if m < 40:
        failed = True

if failed or percentage < 40:
    result = "Fail"
else:
    result = "Pass"

print("\n" + "=" * 35)
print("          MARKSHEET")
print("=" * 35)
print("Name       :", student_name)
print("Roll No    :", roll_no)
print("-" * 35)
for i in range(5):
    print(f"Subject {i + 1}  : {marks[i]}")
print("-" * 35)
print("Total      :", total, "/ 500")
print("Percentage :", round(percentage, 2), "%")
print("Grade      :", grade)
print("Result     :", result)
print("=" * 35)
