hall_length = float(input())
hall_width = float(input())
wardrobe = float(input())

hall_area = (hall_length * 100) * (hall_width * 100)
wardrobe_area = pow(wardrobe * 100, 2)
bench_area = hall_area / 10
area_left = hall_area - wardrobe_area - bench_area

dancer_count = area_left // 7040
print(int(dancer_count))
