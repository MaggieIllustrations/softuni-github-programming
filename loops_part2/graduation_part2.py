student_name = input()
grades_passed = 1
sum_marks = 0
is_expelled = 0
grades_failed = 0

while grades_passed <= 12:
    current_mark = float(input())
    if current_mark >= 4:
        grades_passed += 1
        sum_marks += current_mark
    else:
        grades_failed += 1
        if grades_failed == 2:
            is_expelled = True
            print(f"{student_name} has been excluded at {grades_passed} grade")
            break
if not is_expelled:
    average_grade = sum_marks / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")

