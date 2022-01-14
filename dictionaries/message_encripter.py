import re

patterns = r"([*@])(?P<word>[A-Z][a-z]{2,})(\1)(: \[)(?P<one>[A-Za-z])(\]\|\[)(?P<two>[A-Za-z])(\]\|\[)(?P<three>[A-Za-z])(\]\|)$"

how_many = int(input())

for _ in range(how_many):
    what = input()
    checker = re.search(patterns, what)
    if checker:
        word = checker.group("word")
        one = checker.group("one")
        two = checker.group("two")
        three = checker.group("three")
        print(f"{word}: {ord(one)} {ord(two)} {ord(three)}")
    else:
        print("Valid message not found!")