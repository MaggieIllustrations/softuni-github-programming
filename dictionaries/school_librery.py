shelf = input().split("&")
line = input().split(" | ")

while line[0] != "Done":
    command = line[0]
    book = line[1]  # може и е по-добре да е тук, за да не се повтаря на всякъде

    if command == "Add Book":
        # for book in line[1:]: излишно e
        if book not in shelf:
            shelf.insert(0, book)
    elif command == "Take Book":
        if book in shelf:
            shelf.remove(book)
    elif command == "Swap Books":
        book_2 = line[2]
        if book in shelf and book_2 in shelf:
            book_idx = shelf.index(book)
            book_2_idx = shelf.index(book_2)
            shelf[book_idx], shelf[book_2_idx] = shelf[book_2_idx], shelf[book_idx]
    elif command == "Insert Book":
        # shelf.remove(book) няма как да кажеш remove на нещо, което още не си append-нал :D :D
        shelf.append(book)
    elif command == "Check Book":
        index = int(line[1])
        if not index > len(shelf):  # If the index is invalid, ignore the command.
            print(shelf[index])

    line = input().split(" | ")

print(", ".join(shelf))