upper_limit1 = int(input())
upper_limit2 = int(input())
upper_limit3 = int(input())

if upper_limit1 and upper_limit2 and upper_limit3 in range(1, 9):
    for x in range(1, upper_limit1 + 1):
        if x % 2 != 0:
            continue
        for y in range(1, upper_limit2 + 1):
            if type(y) != int or y not in range(2, 7):
                continue
            for z in range(1, upper_limit3 + 1):
                if z % 2 != 0:
                    continue
                print(f"{x} {y} {z}")
