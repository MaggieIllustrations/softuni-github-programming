sea = input()
cabin_type = input()
nights_count = int(input())

if sea == "Mediterranean":
    if cabin_type == "standard cabin":
        price_per_night = 27.5
    elif cabin_type == "cabin with balcony":
        price_per_night = 3.20
    elif cabin_type == "apartment":
        price_per_night = 40.5
elif sea == "Adriatic":
    if cabin_type == "standard cabin":
        price_per_night = 22.9
    elif cabin_type == "cabin with balcony":
        price = 25.00
    elif cabin_type == "apartment":
        price_per_night = 34.9
elif sea == "Aegean":
    if cabin_type == "standard cabin":
        price_per_night = 23.00
    elif cabin_type == "cabin with balcony":
        price = 26.60
    elif cabin_type == "apartment":
        price_per_night = 39.8
total_cost = price_per_night * 4 * nights_count
if nights_count > 7:
    total_cost -= total_cost * 0.25
print(f"Annie's holiday in the {sea} sea costs {total_cost:.2f} lv.")



