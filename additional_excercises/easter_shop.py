eggs_count = int(input())
sold_eggs = 0
command = input()

while command != "Close":
    if command == "Fill":
        to_fill = int(input())
        eggs_count += to_fill
    if command == "Buy":
        count = int(input())
        if count <= eggs_count:
            eggs_count += count
            sold_eggs += count
        else:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_count}.")
            break
    command = input()
if command == "Close":
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")




