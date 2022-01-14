n = int(input())
l = int(input())

for first in range(1, n):
    for second in range(1, n):
        for third in range(97, 97 + l):
            for fourth in range(97, 97 + l):
                for fifth in range(1, n + 1):
                    third_as_chr = chr(third)
                    fourth_as_chr = chr(fourth)
                    if fifth > first and fifth > second:
                        print(f"{first}{second}{third_as_chr}{fourth_as_chr}{fifth}", end=" ")


