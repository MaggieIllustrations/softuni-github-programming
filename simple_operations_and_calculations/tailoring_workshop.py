tables_count = int(input())
table_length = float(input())
table_width = float(input())

tablecloth_area = ((table_length + 0.60) * (table_width + 0.60)) * tables_count
square_area = (table_length/2) * (table_length/2) * tables_count

dollars = tablecloth_area * 7 + square_area * 9
leva = dollars * 1.85

print(f"{dollars:.2f} USD")
print(f"{leva:.2f} BGN")








