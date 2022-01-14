first = int(input())
second = int(input())
third = int(input())

total_seconds = first + second + third
minutes = total_seconds // 60
seconds = total_seconds % 60

print(f"{minutes}:{seconds:02d}") # vodeshta nula