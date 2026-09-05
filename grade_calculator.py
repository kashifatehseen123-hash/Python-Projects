print("Student Grade Calculator")

name = input("Enter student name: ")

marks = []

for i in range(3):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

average = sum(marks) / len(marks)

print("\n--- Result ---")
print("Student:", name)
print("Average:", average)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)