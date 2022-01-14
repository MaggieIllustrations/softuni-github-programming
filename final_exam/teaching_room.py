import math
room_length = float(input())
room_width = float(input())
if 3 <= room_width <= room_length <= 100:
    column_numbers = (room_width * 100 - 100) // 70
    row_numbers = room_length * 100 // 120
    total_places = column_numbers * row_numbers - 3
    print(math.floor(total_places))



