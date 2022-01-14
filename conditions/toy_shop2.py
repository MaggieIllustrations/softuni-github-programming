holiday_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = puzzle_count * 2.60
dolls_price = dolls_count * 3
teddy_bears_price = teddy_bears_count * 4.10
minions_price = minions_count * 8.20
trucks_price = trucks_count * 2

total_price = puzzle_price + dolls_price + teddy_bears_price + minions_price + trucks_price
toys_count = puzzle_count + dolls_count + teddy_bears_count + minions_count + trucks_count

if toys_count >= 50:
    discounted_price = total_price * 0.25
    end_price = total_price - discounted_price
    rent = end_price * 0.1
    earning = end_price - rent
    if earning >= holiday_price:
        money_left = earning - holiday_price
        print(f"Yes! {money_left:.2f} lv left.")
    else:
        money_left = holiday_price - earning
        print(f" Not enough money! {money_left:.2f} lv needed.")
else:
    if toys_count <= 50:
        end_price = total_price
        rent = end_price * 0.1
        earning = end_price - rent
        if earning <= holiday_price:
            money_left = holiday_price - earning
            print(f"Not enough money! {money_left:.2f} lv needed.")
