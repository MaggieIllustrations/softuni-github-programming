number = input()


def get_sums(type_numbers, number):
    result = 0
    if type_numbers == "even":
        result = sum(list(map(int, filter(lambda x: int(x) % 2 == 0, number))))
    elif type_numbers == "odd":
        result = sum(list(map(int, filter(lambda x: int(x) % 2 == 1, number))))

    return result


evens_sum = get_sums("even", number)
odds_sum = get_sums("odd", number)
print(f"Odd sum = {odds_sum}, Even sum = {evens_sum}")

