import math
astronauts_num = 0
# Input:
ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
avg_astronaut_height = float(input())

spacecraft_volume = ship_height * ship_length * ship_width
avg_astronaut_height_checkup = avg_astronaut_height + 0.40
room_per_astronaut = avg_astronaut_height_checkup * 2 * 2

astronauts_num = math.floor(spacecraft_volume / room_per_astronaut)
if 3 > astronauts_num < 10:
    print(f'The spacecraft holds {astronauts_num} astronauts.')
elif astronauts_num < 3:
    print('The spacecraft is too small.')
elif astronauts_num > 10:
    print('The spacecraft is too big.')