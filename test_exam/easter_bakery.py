flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs = int(input())
yeast = int(input())

sugar_price = flour_price * 0.75
eggs_price = flour_price * 1.1
yeast_price = sugar_price * 0.2

flour_sum = flour_price * flour_kg
sugar_sum = sugar_price * sugar_kg
eggs_sum = eggs_price * eggs
yeast_sum = yeast_price * yeast
total_sum = flour_sum + sugar_sum + eggs_sum + yeast_sum
print(f"{total_sum:.2f}")