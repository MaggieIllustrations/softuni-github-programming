square_meters = float(input())
price = float(7.61)
discount = float(0.18)
whole_price = price * square_meters
discount_price = whole_price * discount
final_price = whole_price - discount_price

print(f" The final price is: {final_price:.2f} lv.")
print(f" The discount is: {discount_price:.2f} lv.")





