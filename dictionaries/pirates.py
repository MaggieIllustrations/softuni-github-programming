cities = {}

while True:
    first_line = input()
    if first_line == "Sail":
        break

    tokens = first_line.split("||")
    city = tokens[0]
    population = int(tokens[1])
    gold = int(tokens[2])

    if city not in cities:
        cities[city] = []
        cities[city].append(population)
        cities[city].append(gold)

    else:
        cities[city][0] += population
        cities[city][1] += gold

while True:
    second_line = input()
    if second_line == "End":
        break

    tokens = second_line.split("=>")
    command = tokens[0]

    if command == "Plunder":
        city = tokens[1]
        people = int(tokens[2])
        gold = int(tokens[3])
        cities[city][0] -= people
        cities[city][1] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[city][0] <= 0 or cities[city][1] <= 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")

    elif command == "Prosper":
        city = tokens[1]
        gold = int(tokens[2])

        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[city][1] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city][1]} gold.")

length = len(cities)

if length > 0:
    print(f"Ahoy, Captain! There are {length} wealthy settlements to go to:")
    ordered_cities = dict(sorted(cities.items(), key=lambda x: (-x[1][1], x[0])))
    for key, value in ordered_cities.items():
        people = value[0]
        gold = value[1]
        print(f"{key} -> Population: {people} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")