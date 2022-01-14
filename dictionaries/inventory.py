#You will receive a journal with some Collecting items, separated with ', ' (comma and space). After that, until receiving "Craft!" you will be receiving different commands.
#Commands (split by " - "):
#"Collect - {item}" – Receiving this command, you should add the given item in your inventory. If the item already exists, you should skip this line.
#"Drop - {item}" – You should remove the item from your inventory, if it exists.
#"Combine Items - {oldItem}:{newItem}" – You should check if the old item exists, if so, add the new item after the old one. Otherwise, ignore the command.
#"Renew – {item}" – If the given item exists, you should change its position and put it last in your inventory.
def check_item_exist(check_item, all_items):
    all_items = set(all_items) # set method is used to extract only the unique elements from a list
    if check_item in all_items:
        return True
    else:
        return False
items = input().split(", ")
command = input()
while not command == "Craft!":
    type_command = command.split(" - ")
    item = command.split(" - ")
    is_exist = check_item_exist(item, items)
    if type_command == "Collect" and not is_exist:
        items.append(item)
    elif type_command == "Drop" and is_exist:
        items.remove(item)
    elif type_command == "Combine Items":
        old_item = item.split(":")
        new_item = item.split(":")


