#     7. * Easter Gifts
# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the
# gifts you plan on buying оn a single line,
# separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
#     • "OutOfStock {gift}"
#         ◦ Find the gifts with this name in your collection, if there are any, and change their values to "None".
#     • "Required {gift} {index}"
#         ◦ Replace the value of the current gift on the given index with this gift, if the index is valid.
#     • "JustInCase {gift}"
#         ◦ Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None", separated by a
# single space in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
#
# gift_count = 0
# gift_word = ' gift'
# gift_count += 1
# gift_word += str(gift_count)
# gift_list += gift_word
gift = ''
gift_list = str(input())
user_command = str(input())
user_command_checkup = {f"OutOfStock {gift}", f"Required {gift} {index}", f"JustInCase {gift}"}
while user_command in user_command_checkup:
    if user_command in
print(gift_list)