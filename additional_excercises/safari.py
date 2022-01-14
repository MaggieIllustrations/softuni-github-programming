budget = float(input())
fuel_needed = int(input())
day_of_the_weekend = input()

fuel_price = fuel_needed * 2.10
total_with_guide = fuel_price + 100
if day_of_the_weekend == "Sunday":
    total_price_with_discount = total_with_guide * 0.2
    if budget > total_price_with_discount:
        money_left = budget - total_price_with_discount
        print(f"Safari time! Money left {money_left:.2f} lv.")
elif day_of_the_weekend == "Saturday":
    total_price_with_discount = total_with_guide * 0.1
    if budget < total_price_with_discount:
        money_needed = abs(total_price_with_discount - budget)
        print(f"Not enough money! Money needed: {money_needed:.2f} lv.")





