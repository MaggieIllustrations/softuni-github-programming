from math import floor as fl
biscuit_per_day = int(input())
workers_count = int(input())
total_other_factory = int(input())

total_this_factory = 20 * biscuit_per_day * workers_count
total_this_factory += 10 * fl(0.75 * biscuit_per_day * workers_count)

for_print = (total_this_factory-total_other_factory)/total_other_factory*100

print(f"You have produced {total_this_factory} biscuits for the past month.")
if for_print >= 0:
    print(f"You produce {for_print:.2f} percent more biscuits.")
else:
    print(f"You produce {abs(for_print):.2f} percent less biscuits.")