n = int(input())
grades_sum = 0
counter = 0

while True:
    command = input()
    if command == "Finish":
        break
    presentation = command
    current_grades_sum = 0
    for i in range(n):
        grade = float(input())
        current_grades_sum += grade
        grades_sum += grade
        counter += 1
    average_grade = current_grades_sum / n
    print(f"{presentation} - {average_grade:.2f}.")

average = grades_sum / counter
print(f"Student's final assessment is {average:.2f}.")

