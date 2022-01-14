def sum_numbers(a, b):
    result = a + b
    return result


def subtract(a, b):
    return a - b


a = int(input())
b = int(input())
c = int(input())

sum = sum_numbers(a, b)
result = subtract(sum, c)
print(result)
