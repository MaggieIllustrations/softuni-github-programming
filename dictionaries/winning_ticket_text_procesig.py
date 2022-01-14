def check_half(ticket):
    max_symbols_count, temp, max_symbol, temp_symbol = 0, 0, '', ''
    for symbol in ticket:
        if symbol in '@$#^' and temp_symbol == symbol:
            temp += 1
        elif symbol in '@$#^':
            if temp > max_symbols_count:
                max_symbols_count = temp
                max_symbol = temp_symbol
            temp = 1
            temp_symbol = symbol
        else:
            if temp > max_symbols_count:
                max_symbols_count = temp
                max_symbol = temp_symbol
            temp_symbol = ''
            temp = 0
    if max_symbols_count <= temp:
        max_symbols_count = temp
        max_symbol = temp_symbol
    if max_symbols_count >= 6:
        return max_symbols_count, max_symbol
    return 0, ''


def main():
    ticket_list = input().split(', ')
    for ticket in ticket_list:
        ticket = ticket.strip()
        if len(ticket) != 20:
            print('invalid ticket')
        else:
            max_symbol1, symbol1 = check_half(ticket[:10])
            max_symbol2, symbol2 = check_half(ticket[10:])
            if max_symbol1 < max_symbol2:
                total_max = max_symbol1
            else:
                total_max = max_symbol2
            if max_symbol1 == 10 and max_symbol2 == 10 and symbol1 == symbol2:
                print(f'ticket "{ticket}" - {total_max}{symbol1} Jackpot!')
            elif 6 <= max_symbol1 and 6 <= max_symbol2 and symbol1 == symbol2:
                print(f'ticket "{ticket}" - {total_max}{symbol1}')
            else:
                print(f'ticket "{ticket}" - no match')


main()