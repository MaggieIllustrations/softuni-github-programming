n = int(input())

p1 = 0
p2 = 0
p3 = 0

for i in range(1, n + 1):
    number = int(input())

    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1

percent1 = p1 / n * 100
percent2 = p2 / n * 100
percent3 = p3 / n * 100
print(f"{percent1:.2f}%")
print(f"{percent2:.2f}%")
print(f"{percent3:.2f}%")
