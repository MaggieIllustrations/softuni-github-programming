budget = int(input())
season = input()
fishermen_count = int(input())

boat_price = 0
if season == "Spring":
    boat_price = 3000
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
elif season == "Winter":
    boat_price = 2600

discount = 0
if fishermen_count <= 6:
    discount = 0.1
elif 7 <= fishermen_count <= 11:
    discount = 0.15
else:
    discount = 0.25

discount_value = boat_price * discount
expenses = boat_price - discount_value

if fishermen_count % 2 == 0 and season != "Autumn":
    expenses = expenses - expenses * 0.05
if budget >= expenses:
    money_left = budget - expenses
    print(f"Yes! You have {money_left:.2f} leva left.")
if budget < expenses:
    money_needed = expenses - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")

