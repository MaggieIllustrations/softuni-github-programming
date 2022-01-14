character_name = "John"
character_age = "35"
is_male = False
print("There once was a man named " + character_name + ", ")
print("he was" + character_age + " years old.")
print("He really liked the name " + character_name + ", ")
print("but did not like being" + character_age + ".")
# Note
phrase = "Giraffe Academy"
print(phrase[3])
print (phrase.index("G"))
print (phrase.replace("Giraffe", "Elephant")) # replaces one word with another
# working with numbers
print(2)
print(10 % 3)
my_num = -5
print(abs(my_num)) #absolute value
print(pow(3, 2)) # power of
print(max(4, 6)) #max number is 6
print(min(4, 6)) #min number is 4
print(round(3.7))
print(str(my_num) + "my favourite number")
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "!")
print("You are " + age + "!")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2) #int is looking for a whole number
result = float(num1) + float(num2) # float is for decimal numbers
print(result)

color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity:")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love" + celebrity)
# creation of lists
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends[1] = "Mike" # modify e.g 1 is Karen - Mike
print(friends[0])
# using functions with lists
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Creed") #always adds the element at the end
friends.insert(1, "Kelly")
friends.remove("Jim") # removes the element of the list
friends.clear() # clear all the elements of the list
friends.sort() # in a alphabetic order
friend2 = friends.copy() # copy of the list
print(friends)

coordinates = (4, 5) # it can not be changed
coordinates[1] = 10
print(coordinates[1])

# Functions
def sayhi():
    print("Hello User")



