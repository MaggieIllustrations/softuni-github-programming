
hall_length = float(input())
hall_width = float(input())
wardrobe_side = float(input())

hall_area = (hall_length * 100) * (hall_width * 100)
wardrobe_area = (wardrobe_side * 100) * (wardrobe_side * 100)
bench_area = hall_area / 10
free_space = hall_area - wardrobe_area - bench_area
dancers_number = free_space / (40 + 7000)
print(int(dancers_number))
