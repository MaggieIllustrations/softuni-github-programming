numbers_as_text = input().split(" ")
sorted_numbers = sorted(numbers_as_text, reverse=True)

print("".join(sorted_numbers))