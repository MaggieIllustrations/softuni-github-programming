
record_seconds = float(input())
distance_meters = float(input())
time_seconds = float(input())

required_climbing_time = distance_meters * time_seconds
time_in = distance_meters // 50
required_climbing_time = required_climbing_time + (time_in * 30)
if required_climbing_time < record_seconds:
    print(f"Yes! The new record is {required_climbing_time:.2f} seconds.")
else:
    print(f"No! He was {(required_climbing_time - record_seconds):.2f} seconds slower.")
