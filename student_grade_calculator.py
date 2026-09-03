# 1. Take student name input
name = input("Enter student name: ")

# 2. Take integer marks for 3 subjects
mark1 = int(input("Enter marks for subject 1: "))
mark2 = int(input("Enter marks for subject 2: "))
mark3 = int(input("Enter marks for subject 3: "))

# 3. Calculate total and average
total_marks = mark1 + mark2 + mark3
average = total_marks / 3

# 4. Determine grade based on average
if average >= 80:
    grade = "A+"
elif average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

# Round the average to 2 decimal places before printing
average = round(average, 2)

# 5. Display simple output
print(f"\nStudent Name: {name}")
print(f"Total Marks: {total_marks}")
print(f"Average: {average}")
print(f"Grade: {grade}")