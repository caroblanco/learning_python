# LISTS
numbers = [1,2,3,4]
matrix = [[1,2],["a","b"]]
zeros = [0] * 5   # * to repeat the items in the list = [0,0,0,0,0]

combined = zeros + numbers

list(range(10)) # creates a list of numbers from 0 to 9 = [1,2,3,4,5,6,7,8,9]
list("Hello world") # creates a list with each caracter = ['h','e','l','l','o', ... ]

len(numbers)    # length of the list 

# ACCESSING ITEMS
print(numbers[0])   # access by index = 1
print(numbers[-1])  # = 4
print(numbers[0:2]) # = 1,2,
print(numbers[::2]) # a STEP, = 1,3
print(numbers[::-1]) #inverse order

# UNPACKING LISTS
# first = numbers[0]

first, second, third, fourth = numbers
first, second, *other = numbers     # other stores the rest of the numbers, its a new list
first, *other, last = numbers 

# LOOPING OVER LISTS
for number in numbers:
    print(number)

for number in enumerate(numbers):   # prints index and the item, en una cupla (0, 1), (1,2), (2,3), (3,4)
    print(number)

for index,number in enumerate(numbers):
    print(index,number)

# ADDING ITEMS
# at the end
numbers.append(5)

# at a specific position
numbers.insert(0,0) # list.insert(index,smth)

# REMOVING ITEMS
# at the end, removes the last item
numbers.pop()

# at a specific position
numbers.pop(0)

# dont know the index
numbers.remove(1)   # removes the FIRST occurance of what you want to remove

# a range of items
del numbers[0:3]

# all the objects
numbers.clear()

# FINDING OBJECTS
numbers.index(1)    # returns the index of what you are looking for in the list (first occurance of what you are looking)

numbers.count(1)    # returns the number of occurances given in the list

x in list           # returns true or false if x is in the list

# copy
list2 = list1.copy()

# SORTING LISTS
numbers2 = [62,2,13,0]
numbers2.sort() # ascendant order, MODIFYS DE OLD LIST
numbers2.sort(reverse = True)

sorted(numbers) #CREATES A NEW LIST
sorted(numbers, reverse=True)

# TUPLES

numbers = (1,2,3,4)
#we CANT change a tuple, only get info about it

numbers[0]

#UNPACKING TUPLES
coordinates=(1,2,3)
x,y,z = coordinates # its the same as x=coordinates[0] y=coordinates[1] z=coordinates[2]


# LAMBDAS
items = [
    ("p1",10),
    ("p2",9),
    ("p3",12),
]

items.sort(key=lambda item:item[1])        #lambda parameters:expression

# def sort_item(item):
#      return item[1]

# MAP FUNCTION

#DICTIONARIES
customer = {
    "name" = "Caro",
    "age"=21
}

#to access
customer["name"] #returns de info of that key => dictionary[key]

#ex
message = input(">")
split_message = message.split(' ')

emojis ={
    ":)" = ":D",
    ":(" = ":P"
}
output =""
for word in split_message:
    output += emojis.get(word, word) + " "

print(output)