bitcoin = int(input())
yan = float(input())
commission = float(input())
commission = commission * 0.01
all_euro = (yan * 0.15 * 1.76 + bitcoin * 1168) / 1.95
charge = all_euro * commission
result = all_euro - charge
print(f"{result:.2f}")




