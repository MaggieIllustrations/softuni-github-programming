text = input()

new_word = ""
for index, letter in enumerate(text):
    if index % 2 == 1:
        new_word += letter
        print(new_word)

