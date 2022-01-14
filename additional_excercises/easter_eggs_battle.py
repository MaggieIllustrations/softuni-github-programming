eggs_number_first_player = int(input())
eggs_number_second_player = int(input())
points_first_player = 0
points_second_player = 0
winner = ''
while winner != "End of battle":
    winner = input()
    if winner == "one":
        eggs_number_second_player = eggs_number_second_player - 1
    elif winner == "two":
        eggs_number_first_player = eggs_number_first_player - 1
    if eggs_number_first_player == 0:
        print(f"Player one is out of eggs. Player two has {eggs_number_second_player} eggs left.")
    elif eggs_number_second_player == 0:
        print(f"Player two is out of eggs. Player one has {eggs_number_first_player} eggs left. ")
print(f"Player one has {eggs_number_first_player} eggs left.")
print(f"Player two has {eggs_number_second_player} eggs left.")


