fruit = input()
set_type = input()
set_count = int(input())

price = 0
if set_type == "small":
    if fruit == "Watermelon":
        price = set_count * 2 * 56
    elif fruit == "Mango":
        price = set_count * 2 * 36.66
    elif fruit == "Pineapple":
        price = set_count * 2 * 42.10
    elif fruit == "Raspberry":
        price = set_count * 2 * 20
if set_type == "big":
    if fruit == "Watermelon":
        price = set_count * 5 * 28.70
    elif fruit == "Mango":
        price = set_count * 5 * 19.60
    elif fruit == "Pineapple":
        price = set_count * 5 * 24.80
    elif fruit == "Raspberry":
        price = set_count * 5 * 15.20

if price >= 400 and price <= 1000:
    price = (85 * price) / 100
if price > 1000:
    price = price / 2
print(f"{price:.2f} lv.")
