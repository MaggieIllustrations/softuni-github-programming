tabs_open = int(input())
salary = int(input())

for _ in range(tabs_open):
    current = input()
    if current == "Facebook":
        salary -= 150
    elif current == "Instagram":
        salary -= 100
    elif current == "Reddit":
        salary -= 50
    if salary <= 0:
        break
if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)

