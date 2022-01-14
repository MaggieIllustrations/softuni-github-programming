
start_points = int(input())
points = start_points
moves_counter = 0

while points > 0:
    move_type = input()
    moves_counter += 1
    if move_type == "bulleseye":
        break

    current_points = int(input())
    if move_type == "double ring":
        current_points *= 2
    elif move_type == "triple ring":
        current_points *= 3
    points -= current_points
if points == 0:
    print(f"Congratulations! You won the game in {moves_counter} moves!")
elif points > 0:
    print(f"Congratulations! You won the game with a bullseye in {moves_counter} moves!")
elif points < 0:
    print(f"Sorry, you lost. Score difference: {abs(points)}.")
