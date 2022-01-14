command = input()
sum_numbers = 0
while command != "Stop":
    curr_number = int(command)
    sum_numbers = sum_numbers + curr_number
    command = input()
print(sum_numbers)
