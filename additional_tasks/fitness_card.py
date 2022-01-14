money = float(input())
gender = input()
age = int(input())
sport = input()

total_money = 0
if age >= 5 and age <= 105 and money >= 10 and money < 1000:
    if gender == "m":
        if sport == "Gym":
            total_money = 42
        elif sport == "Boxing":
            total_money = 41
        elif sport == "Yoga":
            total_money = 45
        elif sport == "Zumba":
            total_money = 34
        elif sport == "Dances":
            total_money = 51
        elif sport == "Pilates":
            total_money = 39
    elif gender == "f":
        if sport == "Gym":
            total_money = 35
        elif sport == "Boxing":
            total_money = 37
        elif sport == "Yoga":
            total_money = 42
        elif sport == "Zumba":
            total_money = 31
        elif sport == "Dances":
            total_money = 53
        elif sport == "Pilates":
            total_money = 37
    if age <= 19:
        total_money -= total_money * 0.2
    if total_money <= money:
        print(f"You purchased a 1 month pass for {sport}.")
    else:
        print(f"You don't have enough money! You need ${total_money - money:.2f} more.")
