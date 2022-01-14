easter_bread = int(input())
eggs = int(input())
cookies = int(input())

easter_bread_price = easter_bread * 3.20
eggs_price = eggs * 4.35
cookies_price = cookies * 5.40
eggs_colour_price = eggs * 12 * 0.15
total_price = easter_bread_price + eggs_price + cookies_price + eggs_colour_price
print(f"{total_price:.2f}")



