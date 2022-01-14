price_hour_per_person = 0
total_sum = 0
# disc:
discount = 0
# az
month = str(input())
hours_spent = int(input())
people_count = int(input())
day_time = str(input())
# proverkite
# prolet
if month == "march" or month == "april" or month == "may":
    if day_time == "day":
        price_hour_per_person = 10.5
    elif day_time == "night":
        price_hour_per_person = 8.4
# lqto
elif month == "june" or month == "july" or month == "august":
    if day_time == "day":
        price_hour_per_person = 12.6
    elif day_time == "night":
        price_hour_per_person = 10.2
#
if people_count >= 4 or hours_spent >= 5:
    if people_count >= 4:
        price_hour_per_person *= 0.9
    else:
        pass
    if hours_spent >= 5:
        price_hour_per_person *= 0.5
    else:
        pass
total_sum = price_hour_per_person * hours_spent * people_count
# izhod
print(f"Price per person for one hour: {price_hour_per_person:.2f}")
print(f"Total cost of the visit: {total_sum:.2f}")