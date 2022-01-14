import math

type_sushi = input()
name_restaurant = input()
portions_count = int(input())
order = input()
price_order = 0
rest_array = ["Sushi Zone", "Sushi Time", "Sushi Bar", "Asian Pub"]

if name_restaurant == "Sushi Zone":
    if type_sushi == "sashimi":
        price = 4.99
        price_order = portions_count * price
    elif type_sushi == "maki":
        price = 5.29
        price_order = portions_count * price
    elif type_sushi == "uramaki":
        price = 5.99
        price_order = portions_count * price
    elif type_sushi == "temaki":
        price = 4.29
        price_order = portions_count * price
    if order == "Y":
        price_delivery = price_order * 0.20
        total_price_order = math.ceil(price_order + price_delivery)
        print(f"Total price: {total_price_order} lv.")

    elif order == "N":
        total_price_order = math.ceil(price_order)
        print(f"Total price: {total_price_order} lv.")
elif name_restaurant == "Sushi Time":
    if type_sushi == "sashimi":
        price = 5.49
        price_order = portions_count * price
    elif type_sushi == "maki":
        price = 4.69
        price_order = portions_count * price
    elif type_sushi == "uramaki":
        price = 4.49
        price_order = portions_count * price
    elif type_sushi == "temaki":
        price = 5.19
        price_order = portions_count * price
    if order == "Y":
        price_delivery = price_order * 0.20
        total_price_order = math.ceil(price_order + price_delivery)
        print(f"Total price: {total_price_order} lv.")

    elif order == "N":
        total_price_order = math.ceil(price_order)
        print(f"Total price: {total_price_order} lv.")
elif name_restaurant == "Sushi Bar":
    if type_sushi == "sashimi":
        price = 5.25
        price_order = portions_count * price
    elif type_sushi == "maki":
        price = 5.55
        price_order = portions_count * price
    elif type_sushi == "uramaki":
        price = 6.25
        price_order = portions_count * price
    elif type_sushi == "temaki":
        price = 4.75
        price_order = portions_count * price
    if order == "Y":
        price_delivery = price_order * 0.20
        total_price_order = math.ceil(price_order + price_delivery)
        print(f"Total price: {total_price_order} lv.")

    elif order == "N":
        total_price_order = math.ceil(price_order)
        print(f"Total price: {total_price_order} lv.")
elif name_restaurant == "Asian Pub":
    if type_sushi == "sashimi":
        price = 4.50
        price_order = portions_count * price
    elif type_sushi == "maki":
        price = 4.80
        price_order = portions_count * price
    elif type_sushi == "uramaki":
        price = 5.50
        price_order = portions_count * price
    elif type_sushi == "temaki":
        price = 5.50
        price_order = portions_count * price
    if order == "Y":
        price_delivery = price_order * 0.20
        total_price_order = math.ceil(price_order + price_delivery)
        print(f"Total price: {total_price_order} lv.")

    elif order == "N":
        total_price_order = math.ceil(price_order)
        print(f"Total price: {total_price_order} lv.")
#
elif name_restaurant not in rest_array:
    print(f"{name_restaurant} is invalid restaurant!")

