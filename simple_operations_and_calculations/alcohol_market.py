whisky_price_in_bgn = float(input())
beer_in_liters = float(input())
whine_in_liters = float(input())
schnapps_in_liters = float(input())
whisky_in_liters = float(input())

schnapps_price = float(whisky_price_in_bgn / 2)
whine_price = schnapps_price - (0.4 * schnapps_price)
beer_price = schnapps_price - (0.8 * schnapps_price)
#
# whine_price = schnapps_price - (whine_price * schnapps_price)
# beer_price = schnapps_price - (beer_price * schnapps_price)
amount_for_the_schnapps = schnapps_in_liters * schnapps_price
whine_amount = whine_in_liters * whine_price
beer_amount = beer_in_liters * beer_price
whisky_amount = whisky_in_liters * whisky_price_in_bgn
total_amount = amount_for_the_schnapps + whine_amount + beer_amount + whisky_amount

print(f"{total_amount:.2f}")