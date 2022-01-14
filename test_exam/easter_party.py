guests_count = int(input())
voucher_price = float(input())
desi_budget = float(input())

if guests_count >= 10 and guests_count <= 15:
    voucher_price = voucher_price * 0.85
elif guests_count > 15 and guests_count <= 20:
    voucher_price = voucher_price * 0.8
elif guests_count > 20:
    voucher_price = voucher_price * 0.75

cake_price = desi_budget * 0.1
total_amount_party = guests_count * voucher_price + cake_price
if total_amount_party >= desi_budget:
    leva_left_budget_min_total = abs(total_amount_party - desi_budget)
    print(f"No party! {leva_left_budget_min_total:.2f} leva needed.")
    #
else:
    leva_left = abs(desi_budget - total_amount_party)
    print(f"It is party time! {leva_left:.2f} leva left.")


