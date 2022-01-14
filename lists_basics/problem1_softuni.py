skill = input()
command = input()

while command != "For Azeroth":
    command = command.split(" ")
    command = command[0]
    if command == "GladiatorStance":
        skill = skill.upper()
        print(skill)
        break
    elif command == "DefensiveStance":
        skill = skill.lower()
        print(skill)
        break
    elif command == "Dispel":
        index = command[1]
        letter = command[2]
        if index > len(skill) - 1 or index < 0:
            skill = skill.remove(index, 1)
            skill = skill.insert(index, letter)
            print("Dispel too weak")
        else:
            print("Success!")
            break




















