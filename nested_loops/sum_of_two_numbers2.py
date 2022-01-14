start_number = int(input())
end_number = int(input())
magic_number = int(input())
count = 0
is_found = False

for first_number in range(start_number, end_number + 1):

    for second_number in range(start_number, end_number + 1):
        count += 1
        if first_number + second_number == magic_number:
            is_found = True
            print(f"Combination N:{count} ({first_number} + {second_number} = {magic_number})")
            break
    if is_found:
        break
if is_found == False:
    print(f"{count} combinations - neither equals {magic_number}")