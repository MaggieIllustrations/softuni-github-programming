pencils_count = int(input())
markers_count = int(input())
liquid = float(input())
discount = int(input())

price_pencils = pencils_count * 5.80
price_markers = markers_count * 7.20
price_liquid = liquid * 1.20
price_all_materials = price_pencils + price_markers + price_liquid
price_with_discount = price_all_materials - ((price_all_materials * discount)/100)
print(f"{price_with_discount:.3f}")