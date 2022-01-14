initial_energy = int(input())

strike = 0
win = True

command = input()

while not command == "End of battle":
    distance = int(command)
    initial_energy -= distance
    strike += 1

else:
    strike % 3 == 0:
    initial_energy += strike

    if initial_energy < distance:
        print(f"Not enough energy! Game ends with {strike} won battles and {initial_energy} energy")
        win = False
        break

    command = input()

if win:
    print(f"Won battles: {strike}. Energy left: {initial_energy}")