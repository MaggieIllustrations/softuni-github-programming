number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegetarian_menu = int(input())

price_chicken_menu = number_chicken_menu * 10.35
price_fish_menu = number_fish_menu * 12.40
price_vegetarian_menu = number_vegetarian_menu * 8.15
total_price_menu = price_chicken_menu + price_fish_menu + price_vegetarian_menu

dessert_price = total_price_menu * 0.2
delivery_price = 2.50
total_price_order = total_price_menu + dessert_price + delivery_price
print(f"Total: {total_price_order:.2f}")

