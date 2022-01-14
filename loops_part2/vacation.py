money_for_vacation = float(input())
saved_money = float(input())
days = 1
spending_days_count = 0

while True:
    command = input()
    money = float(input())
    if command == "save":
        saved_money += money
        spending_days_count = 0
        if saved_money >= money_for_vacation:
            print(f"You saved the money for {days} days.")
            break
    elif command == "spend":
        saved_money -= money
        if saved_money < 0:
            saved_money = 0
        spending_days_count += 1
        if spending_days_count == 5:
            print("You can't save the money.")
            print(days)
            break
    days += 1


