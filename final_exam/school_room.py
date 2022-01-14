import math
i = float(input()) # room length
w = float(input()) # room width
# Output:
num_seats = 0
# workplace: 70 * 120
corridor = 100
# Entrance  - 1 workplace
# katedra = - 2 workplaces
workplace_space_needed = 70 * 120
#
katedra = workplace_space_needed * 2
entrance = workplace_space_needed
room_space = i * 100 * w * 100

#
room_left = room_space - (katedra + entrance + corridor * w)
num_seats = room_left / workplace_space_needed
print(math.floor(num_seats))