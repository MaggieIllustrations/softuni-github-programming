n = int(input())
for powerof in range(n + 1):
    if powerof % 2 == 0:
        value = pow(2, powerof)
        print(value)