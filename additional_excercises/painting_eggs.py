eggs_size = input()
eggs_colour = input()
eggs_number = int(input())

price = 0
if eggs_colour == "Red":
    if eggs_size == "Large":
        price = 16
    elif eggs_size == "Medium":
        price = 13
    elif eggs_size == "Small":
        price = 9
elif eggs_colour == "Green":
    if eggs_size == "Large":
        price = 12
    elif eggs_size == "Medium":
        price = 9
    elif eggs_size == "Small":
        price = 8
elif eggs_colour == "Yellow":
    if eggs_size == "Large":
        price = 9
    elif eggs_size == "Medium":
        price = 7
    elif eggs_size == "Small":
        price = 5
egg_price = eggs_number * price
money_paid = egg_price * 0.35
amount_after_money_paid = egg_price - money_paid
print(f"{amount_after_money_paid:.2f} leva.")




