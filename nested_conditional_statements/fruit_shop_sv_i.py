fruit = str(input())
fruit = fruit.lower()
day = str(input())
day = day.lower()
quantity = float(input())
workday_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
if day in workday_list:
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
    price *= quantity
    print(f"{price:.2f}")
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
    price *= quantity
    print(f"{price:.2f}")
else:
    print("error")