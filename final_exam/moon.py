import math
speed = float(input())
fuel = float(input())
time_spend = 3

distance = 384400
time = math.ceil(distance * 2) / speed
time = time + time_spend
overall_fuel = (fuel * distance * 2) / 100
print(math.ceil(time))
print(math.ceil(overall_fuel))


