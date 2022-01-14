first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    evens_sum = 0
    odd_sum = 0
    counter = 1
    number_copy = number

    while number_copy > 0:
        last = number_copy % 10
        if counter % 2 == 0:
            evens_sum += last
        else:
            odd_sum += last
        number_copy = number_copy // 10
        counter += 1

    if evens_sum == odd_sum:
        print(number, end=" ")

