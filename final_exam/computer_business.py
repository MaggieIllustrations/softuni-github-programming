price_hour_per_person = 0
total_sum = 0
# DISCOUNT VARIABL:
discount = 0
# USER INPUT
month = str(input())
hours_spent = int(input())
participants_num = int(input())
day_time = str(input())
# checkups
# spring
if month == "march":
    if day_time == "day":
        price_hour_per_person = 10.5
    elif day_time == "night":
        price_hour_per_person = 8.4
elif month == "april":
    if day_time == "day":
        price_hour_per_person = 10.5
    elif day_time == "night":
        price_hour_per_person = 8.4
elif month == "may":
    if day_time == "day":
        price_hour_per_person = 10.5
    elif day_time == "night":
        price_hour_per_person = 8.4
# Summer time:
elif month == "june":
    if day_time == "day":
        price_hour_per_person = 12.6
    elif day_time == "night":
        price_hour_per_person = 10.2
elif month == "july":
    if day_time == "day":
        price_hour_per_person = 12.6
    elif day_time == "night":
        price_hour_per_person = 10.2
elif month == "august":
    if day_time == "day":
        price_hour_per_person = 12.6
    elif day_time == "night":
        price_hour_per_person = 10.2
#
discounter = False
if participants_num >= 4 or hours_spent >= 5:
    discounter = True
    if participants_num >= 4:
        price_hour_per_person *= 0.9
    else:
        pass
    if hours_spent >= 5:
        price_hour_per_person *= 0.5
    else:
        pass
# price_hour_per_person *= discount
# discounted = price_hour_per_person * discount
# discount_sum = price_hour_per_person * hours_spent
total_sum = price_hour_per_person * hours_spent * participants_num
# OUTPUT
print(f"Price per person for one hour: {price_hour_per_person:.2f}")
print(f"Total cost of the visit: {total_sum:.2f}")