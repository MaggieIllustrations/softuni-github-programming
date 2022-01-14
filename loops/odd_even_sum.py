nums_list = int(input())
diff = 0
sum_of_odd = 0
sum_of_even = 0
for i in range(nums_list):
    user_input_prompt = int(input())
    if i % 2 == 0:
        sum_of_even += user_input_prompt
    else:
        sum_of_odd += user_input_prompt
if sum_of_even == sum_of_odd:
    print(f"Yes\nSum = {sum_of_even}")
else:
    diff = abs(sum_of_even - sum_of_odd)
    print(f"No\nDiff = {diff}")