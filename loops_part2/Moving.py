width = int(input())
length = int(input())
height = int(input())

space_volume = width * length * height
free_space = space_volume
is_done_moving = False
while free_space > 0:
    command = input()
    if command == "Done":
        is_done_moving = True
        break
    boxes_count = int(command)
    free_space -= boxes_count
if is_done_moving:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")


