age = float(input())
gender = input()

if gender == "f" and age < 16:
    print("Miss")
elif gender == "f" and age >= 16:
    print("Ms.")
elif gender == "m" and age < 16:
    print("Master")
elif gender == "m" and age >= 16:
    print("Mr.")

# gender_char = gender.lower() [0] за принтиране на малки букви на конзолата, но тогава трябва да се промени gender с gender_char
# и проверките се правят с  него 