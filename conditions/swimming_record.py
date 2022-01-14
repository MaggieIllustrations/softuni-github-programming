
record_seconds = float(input())
distance_meters = float(input())
time_seconds = float(input())

required_swimming_time = distance_meters * time_seconds
time_in = distance_meters // 15
required_swimming_time = required_swimming_time + (time_in * 12.5)
if required_swimming_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {required_swimming_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {(required_swimming_time - record_seconds):.2f} seconds slower.")




