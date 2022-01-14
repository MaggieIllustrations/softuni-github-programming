numbers_as_strings = input().split(" ")
numbers = []

for number in numbers_as_strings:
    numbers.append(-int(number))
    # append добавя int от number, превръща го от стринг в число
print(numbers)
