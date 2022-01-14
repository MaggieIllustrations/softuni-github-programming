speed_information = float(input())

if speed_information <= 10:
    print("slow")
elif speed_information <= 50:
    print("average")
elif speed_information <= 150:
    print("fast")
elif speed_information <= 1000:
    print("ultra fast")
else:
    print("extremely fast")
