def get_smallest_of_three_numbers(a, b, c):
    smallest = c
    if a < b and a < c:
        smallest = a
    elif b < a and b < c:
        smallest = b

    return smallest
a = int(input())
b = int(input())
c = int(input())
result = get_smallest_of_three_numbers(a, b, c)
print(result)