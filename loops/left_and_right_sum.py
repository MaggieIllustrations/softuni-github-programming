nums_list = int(input())
diff = 0
sum_of_one = 0
sum_of_two = 0
for i in range(nums_list):
    user_input_prompt_one = int(input())
    sum_of_one += user_input_prompt_one
for i in range(nums_list):
    user_input_prompt_two = int(input())
    sum_of_two += user_input_prompt_two
if sum_of_one == sum_of_two:
    print(f"Yes, sum = {sum_of_one}")
else:
    diff = abs(sum_of_one - sum_of_two)
    print(f"No, diff = {diff}")