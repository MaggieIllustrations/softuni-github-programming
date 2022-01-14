from math import pi

shape = input()
area = 0.0

if shape == "square":
    side = float(input())
    area = side * side

elif shape == "rectangle":
    rectangle_side_a = float(input())
    rectangle_side_b = float(input())
    area = rectangle_side_a * rectangle_side_b

elif shape == "circle":
    radius = float(input())
    area = pi * radius * radius

elif shape == "triangle":
    side_a = float(input())
    side_s_h = float(input())
    area = side_a * side_s_h / 2

print(f"{area:.3f}")
