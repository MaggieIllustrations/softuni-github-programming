from math import floor

income = float(input())
grade = float(input())
minimal_wage = float(input())

social_scholarship = 0
excellent_scholarship = 0

if income < minimal_wage:
    if grade > 4.5:
        social_scholarship = minimal_wage * 0.35
if grade >= 5.50:
    excellent_scholarship = grade * 25

if social_scholarship > excellent_scholarship:
    if social_scholarship > excellent_scholarship:
        print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
elif excellent_scholarship > social_scholarship:
    print(f"You get a scholarship for excellent results {floor(excellent_scholarship)} BGN")
else:
    print(f"You cannot get a scholarship!")
