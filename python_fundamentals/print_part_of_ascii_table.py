start_ascii_value = int(input())
end_ascii_value = int(input())

for i in range(start_ascii_value, end_ascii_value + 1):
    symbol = chr(i)
    print(symbol, end=" ")


