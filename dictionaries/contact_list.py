contacts = input().split()

while True:
    command = input()
    tokens = command.split()
    action = tokens[0]
    if action == 'Add':
        name = tokens[1]
        if name not in contacts:
            contacts.append(name)
        else:
            index = int(tokens[2])
            if 0 <= index < len(contacts):
                contacts.insert(index, name)
    elif action == 'Remove':
        index = int(tokens[1])
        if 0 <= index < len(contacts):
            contacts.pop(index)
    elif action == 'Export':
        start_index = int(tokens[1])
        count = int(tokens[2])
        if start_index + count > len(contacts):
            print(f"{' '.join(contacts[start_index:])}")
        else:
            print(f"{' '.join(contacts[start_index:start_index + count])}")

    elif action == 'Print':
        way = tokens[1]
        if way == 'Normal':
            print(f"Contacts: {' '.join(contacts)}")
            break
        else:
            print(f"Contacts: {' '.join(contacts[::-1])}")
            break