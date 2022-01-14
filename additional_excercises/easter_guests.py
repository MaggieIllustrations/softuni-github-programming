import math
guests_count = int(input())
budget = int(input())

easter_bread = 4
egg = 0.45

easter_bread_needed = math.ceil(guests_count / 3)
eggs_needed = guests_count * 2
easter_bread_price = easter_bread * easter_bread_needed
eggs_price = egg * eggs_needed
total_price = easter_bread_price + eggs_price
if total_price <= budget:
    money_left = budget - total_price
    print(f"Lyubo bought {easter_bread_needed} Easter bread and {eggs_needed} eggs.")
    print(f"He has {money_left:.2f} lv. left.")
elif total_price >= budget:
    money_needed = abs(total_price - budget)
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {money_needed:.2f} lv. more.")


