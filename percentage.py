
marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks of subject {i} (out of 50): "))
    marks.append(m)

total = sum(marks)
percentage = (total / 250) * 100  
if percentage >= 90 <=100 :
    grade = "O"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "D"
print("\nTotal Marks:", total, "/ 250")
print("Percentage:", percentage, "%")
print("Grade:", grade)
