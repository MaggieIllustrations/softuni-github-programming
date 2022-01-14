def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value

def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))

command = input()

collection_heroes = {}
spell_name = {}

while command != "End":
    args = input().split()
    command = args[0]
    hero_name = args[1]

    if command == "Enroll":
        spell_name = args[2]
        if hero_name in collection_heroes:
            print(f"{collection_heroes[hero_name]} hero name is already enrolled")
            continue

    elif command == "Learn":
        collection_heroes[hero_name] = spell_name
        if hero_name not in collection_heroes:
            print(f"{hero_name} doesn't exist")
        if hero_name in collection_heroes:
            print(f"{hero_name} has already learned {spell_name}")
    elif command == "Unlearn":
        if hero_name not in collection_heroes:
            print(f"{hero_name} doesn't exist")
            continue
        collection_heroes.pop(spell_name)
        if hero_name not in collection_heroes:
            print(f"{hero_name} doesn't know {spell_name}")

collection_heroes = dict(sorted(collection_heroes.items(), key=lambda el: (-el[1], el[0])))
spell_name = dict(sorted(spell_name.items()))

print_dict(collection_heroes, "{}: {}")
print_dict(spell_name, "{}: {}")


