first_char = input()
second_char = input()


def get_chars_in_range(first, second):
    result = []
    min_char = ord(min([first, second]))
    max_char = ord(max([first, second]))
    for i in range(min_char + 1, max_char):
        character = chr(i)
        result.append(character)
    return result


result = get_chars_in_range(first_char, second_char)
print(" ".join(result))
