flower_type = input()
flowers_count = int(input())
budget = int(input())

total_price = 0

if flower_type == "Roses":
    total_price = flowers_count * 5
    if flowers_count > 80:
        total_price = total_price * 0.9
elif flower_type == "Dahlias":
    total_price = flowers_count * 3.8
    if flowers_count > 90:
        total_price = total_price * 0.85
elif flower_type == "Tulips":
    total_price = flowers_count * 2.80
    if flowers_count > 80:
        total_price = total_price * 0.85
elif flower_type == "Narcissus":
    total_price = flowers_count * 3
    if flowers_count < 120:
        total_price = total_price * 1.15
elif flower_type == "Gladiolus":
    total_price = flowers_count * 2.50
    if flowers_count < 80:
        total_price = total_price * 1.2

if budget >= total_price:
    print(f"Hey, you have a great garden with {flowers_count} {flower_type} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")

