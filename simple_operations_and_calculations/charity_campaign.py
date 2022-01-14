days_of_the_campaign = int(input())
confectioner_number = int(input())
cake_number = int(input())
waffle_number = int(input())
pancake_number = int(input())

cake_price = cake_number * 45
waffle_price = waffle_number * 5.80
pancake_price = pancake_number * 3.20
total_sum_for_one_day = (cake_price + waffle_price + pancake_price) * confectioner_number
total_sum_of_the_campaign = total_sum_for_one_day * days_of_the_campaign
sum_after_the_expenses = total_sum_of_the_campaign - (total_sum_of_the_campaign /8)
money_collected = sum_after_the_expenses

print(f"{money_collected:.2f}")



