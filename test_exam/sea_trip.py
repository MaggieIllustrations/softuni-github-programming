food_money_for_one_day = float(input())
souvenirs_money_for_one_day = float(input())
hotel_money_for_one_day = float(input())

road_km = 420
gasoline_needed = 420 / 100 * 7
gasoline_money = gasoline_needed * 1.85
days = 3

money_for_food_and_souvenirs = days * food_money_for_one_day + days * souvenirs_money_for_one_day

first_day = hotel_money_for_one_day * 0.9
second_day = hotel_money_for_one_day * 0.85
third_day = hotel_money_for_one_day * 0.8

total_money = gasoline_money + money_for_food_and_souvenirs + first_day + second_day + third_day
print(f"Money needed: {total_money:.2f}")






