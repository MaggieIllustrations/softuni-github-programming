count_numbers = int(input())

counter = 0
smallest_number = 0
while counter < count_numbers:
    curr_number = int(input())
    if counter == 0:
        smallest_number = curr_number

    elif curr_number < smallest_number:
        smallest_number = curr_number
    counter += 1
print(smallest_number)