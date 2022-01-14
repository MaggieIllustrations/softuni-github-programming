import math
player_name = input()
games_played = int(input())


volleyball_points = 0
volleyball_games_counter = 0
tennis_points = 0
tennis_games_counter = 0
badminton_points = 0
badminton_games_counter = 0

for game in range(games_played):
    game_type = input()
    current_points = int(input())
    if game_type == "volleyball":
        current_points = current_points * 1.07
        volleyball_points += current_points
        volleyball_games_counter += 1
    elif game_type == "tennis":
        current_points = current_points * 1.05
        tennis_points += current_points
        tennis_games_counter += 1
    elif game_type == "badminton":
        current_points = current_points * 1.02
        badminton_points += current_points
        badminton_games_counter += 1
total_points = math.floor(volleyball_points + tennis_points + badminton_points)
volleyball_average = math.floor(volleyball_points / volleyball_games_counter)
tennis_average = math.floor(tennis_points / tennis_games_counter)
badminton_average = math.floor(badminton_points / badminton_games_counter)
if volleyball_average >= 75 and tennis_average >= 75 and badminton_average >= 75:
    print(f"Congratulations, {player_name}! You won the cruise games with {total_points} points.")
else:
    print(f"Sorry, {player_name}, you lost. Your points are only {total_points}.")

