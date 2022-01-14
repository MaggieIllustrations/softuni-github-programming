holiday_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())
            #
total_price_dolls = dolls_count * 3
total_price_puzzles = puzzle_count * 2.6
total_price_teddy_bears = teddy_bears_count * 4.10
total_price_minions = minions_count * 8.20
total_price_trucks = trucks_count * 2
total_price = total_price_puzzles + total_price_dolls + \
              total_price_teddy_bears + total_price_minions + \
              total_price_trucks
total_amount_toys = puzzle_count + dolls_count + teddy_bears_count + minions_count + trucks_count
if total_amount_toys >= 50:
    discount = total_price * 0.25            
    total_price = total_price - discount     
    rent = total_price * 0.1                 
    earning_after_rent = total_price - rent  
    if earning_after_rent >= holiday_price:
        earning_left = earning_after_rent - holiday_price
        print(f"Yes! {earning_left:.2f} lv left.")
   else:
       needed_money = holiday_price - earning_after_rent
       print(f"Not enough money! {needed_money:.2f} lv left.")
else:
    rent = total_price * 0.1
    earning_after_rent = total_price - rent
    if earning_after_rent >= holiday_price:
       earning_left = earning_after_rent - holiday_price
       print(f"Yes! {earning_left:.2f} lv left.")
    else:
       needed_money = holiday_price - earning_after_rent
       print(f"Not enough money! {needed_money:.2f} lv needed.")
