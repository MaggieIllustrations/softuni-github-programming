initial_array_values = input().split(' ')

while True:
    command = input()
    if command == 'End':
        print(', '.join(initial_array_values))
        break
    command = command.split()
    item = command[1]
    if command[0] == 'Swap':
        if item not in initial_array_values:
            initial_array_values.insert(0, item)
    elif command[0] == 'Multiply':
        if item in initial_array_values:
            initial_array_values.remove(item)
    elif command[0] == 'Decrease':
        if item in initial_array_values:
            initial_array_values.remove(item)
            initial_array_values.append(item)

            initial_array_values[int(initial_array_values.index(old_item))] = new_item