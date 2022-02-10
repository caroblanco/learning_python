# COMPARISSON OPERATORS
10 > 3
10 < 3
10 == "10"
10 != 9

"bag" > "apple" # = True (which one is longer)
"bag" == "BAG" # = False

# CONDITIONAL STATEMENTS
temperature = 35

if temperature > 30:
    print("it's warm")
    print("toma awa")
elif temperature > 20:
    print("it's nice")
else:
    print("it's cold")
print("done")   #THIS STATEMENTS ALWAYS EXECUTES

#TERNARY OPERATOR
age = 22

if age >= 18:
    message = "Elegible"
else:
    message = "Not elegible"
print(message)

# or message = "Eligible" if age >= 18 else "Not elegible"

#LOGICAL OPERATORS
#and     or      not

high_income = True
good_credit = True

if high_income and good_credit:
    print("elegible")
else:
    print("not elegible")
# ---------------------------
student = True

if not student:
    print("elegible")
else:
    print("not elegible")
# ----------------------------
if (high_income and good_credit) and not student:
    print("elegible")
else:
    print("not elegible")

# CHAIN COMPARISSON OPERATORS
age = 22

if 19 <= age < 65:      # age >= 18 and age < 65
    print("elegible")

# FOR LOOPS
for i in range(3):  # range is how many times we ant to repeat the statements | i represents the round 
    print("attempt", i)     # = attempt 0     attempt 1       attempt 2

for i in range(1,4):  # i starts in 1
    print("attempt", i) 

for i in range(1,10,2):  # i starts in 1, 2 is the steps, so i = 1 ,3, 5, 7, 9 (se saltea del 1 al 10 cada dos nums)
    print("attempt", i) 

for i in "python":  # each iteration will be after each character of the string
    print(i)

for i in [1,2,3,4]:  # each iteration will be after each object in the list
    print(i)

# FOR... ELSE
successful = True
for i in range(3):
    print("attempt")
    if successful:
        print("successful")
        break   # escapes the loop
else:                                           # the else block executes if the for loop doesnt end early (with the break)
    print("attempted 3 times and failed :(")

# NESTED LOOPS
for i in range(5):
    for j in range(3):
        print(f"({i},{j})")

# WHILE LOOPS
number = 100

while number > 0:
    print(number)
    number //= 2

# --------------------
command = ""

while command.lower() != "quit":    # command != "quit":
    command = input(">")    # INPUT -> RECIVES INFO FROM THE USER
    print("ECHO", command)

#GUESSING GAME
secret_number = 9
guess_count=0
guess_limit = 3

while guess_count<guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if(guess == secret_number):
        print('You won :)')
        break
else:                               #if the while loop completes, we execute this. If it breaks before ending, it doesnt.
    print('You didnt guess :(')

# INFINITE LOOPS
