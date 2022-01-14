town_name = input()
sales_count = float(input())

commission = 0
is_input_valid = True
if town_name == "Sofia" and sales_count >= 0:
    if 0 <= sales_count <= 500:
        commission = 0.05
    elif 500 < sales_count <= 1000:
        commission = 0.07
    elif 1000 < sales_count <= 10000:
        commission = 0.08
    elif sales_count > 10000:
        commission = 0.12
    else:
        print("error")
elif town_name == "Varna" and sales_count >= 0:
    if 0 <= sales_count <= 500:
        commission = 0.045
    elif 500 < sales_count <= 1000:
        commission = 0.075
    elif 1000 < sales_count <= 10000:
        commission = 0.1
    elif sales_count > 10000:
        commission = 0.13
elif town_name == "Plovdiv" and sales_count >= 0:
    if 0 <= sales_count <= 500:
        commission = 0.055
    elif 500 < sales_count <= 1000:
        commission = 0.08
    elif 1000 < sales_count <= 10000:
        commission = 0.12
    elif sales_count > 10000:
        commission = 0.145
else:
    print("error")
    is_input_valid = False
if is_input_valid:
    print(f"{commission * sales_count:.2f}")






