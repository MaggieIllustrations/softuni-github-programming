import math
width_spaceship = float(input())
length_spaceship = float(input())
height_spaceship = float(input())
average_height_astronauts = float(input())

volume_spaceship = width_spaceship * length_spaceship * height_spaceship
volume_room = (average_height_astronauts + 0.40) * 2 * 2
people_count = math.floor(volume_spaceship / volume_room)
if 3 <= people_count <= 10:
    print(f"The spacecraft holds {people_count} astronauts.")
elif people_count < 3:
    print(f"The spacecraft is too small.")
elif people_count > 10:
    print(f"The spacecraft is too big.")





