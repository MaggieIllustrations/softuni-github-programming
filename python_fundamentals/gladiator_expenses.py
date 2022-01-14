lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet_count = 0
broken_sword_count = 0
broken_shield_count = 0
broken_armor_count = 0
for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        broken_helmet_count += 1
    if i % 3 == 0:
        broken_sword_count += 1
    if i % 6 == 0:
        broken_shield_count += 1
    if i % 12 == 0:
        broken_armor_count += 1
total_expenses = broken_helmet_count * helmet_price \
                 + broken_sword_count * sword_price \
                 + broken_shield_count * shield_price + \
                 broken_armor_count * armor_price
print(f"Gladiator expenses: {total_expenses:.2f} aureus")

