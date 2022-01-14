minutes_walk_per_day = int(input())
walks_count_per_day = int(input())
cat_calories_intake = int(input())

total_minutes_walk = minutes_walk_per_day * walks_count_per_day
total_burned_calories = total_minutes_walk * 5
if total_burned_calories >= cat_calories_intake * 0.5:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burned_calories}.")
elif total_burned_calories < cat_calories_intake * 0.5:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burned_calories}.")

