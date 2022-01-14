substrings = input().split(", ")
strings = input().split(", ")

result = []

for substring in substrings:
    for string in strings:
        if substring in string and substring not in result:
            result.append(substring)
print(result)


substrings = input().split(", ")
string = input()

result = [x for x in substrings if x in string]

print(result)