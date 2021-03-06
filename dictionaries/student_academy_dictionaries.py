n = int(input())

students = {}

for i in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(grade)

students_average_grades = {}

for student, grades in students.items():
    average = sum(grades) / len(grades)
    if average < 4.5:
        continue
    students_average_grades[student] = average

students_average_grades = dict(sorted(students_average_grades.items(), key=lambda x: x[1], reverse=True))
for student, average in students_average_grades.items():
    print(f"{student} -> {average:.2f}")





