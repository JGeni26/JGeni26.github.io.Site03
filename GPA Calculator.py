# Taking inputs for marks in each subject

bangla = int(input("Enter marks for Bangla (1-100): "))
english = int(input("Enter marks for English (1-100): "))
math = int(input("Enter marks for Math (1-100): "))
science = int(input("Enter marks for Science (1-100): "))

average = (bangla + english + math + science) / 4

if 91 <= average <= 100:
    grade = 'A+'
elif 81 <= average <= 90:
    grade = 'A'
elif 71 <= average <= 80:
    grade = 'B'
elif 61 <= average <= 70:
    grade = 'C'
elif 41 <= average <= 60:
    grade = 'D'
elif 0 <= average <= 40:
    grade = 'F'
else:
    grade = "invalid"
print(f"\nAverage Marks: {average:.2f}")
print(f"Grade: {grade}")
