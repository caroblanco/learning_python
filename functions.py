# DEFINE A FUNCTION
def greet(first_name, last_name):     # return value by default is None
    print(f"Hi {first_name} {last_name}")
    print("Welcome to Caro's code :3")

def get_greeting(name):
    return f"Hi {name}"

# CALL A FUNCTION
greet("Caro", "Blanco")      # arguments -> actual value for a given parameter
greet("Brisa", "Vite")

get_greeting("Caro")

# KEYWORD ARGUMENTS
def increment(number,by):
    return number + by

print(increment(2, by=1))       # by=1 to make it more READABLE

# DEFAULT ARGUMENTS
def increment2(number,by=1):     # by=1, by's default value is 1 if you dont provide it. Optional parameters go last in the definition
    return number + by

print(increment2(2))  

# *ARGS: if you want to send more arguments than the ones you allow initially
def multiply(x,y):
    return x * y

#multiply(2,3,4,5) NO!!!

#instead...
def multiply2(*numbers):
    print(numbers)     # = (2,3,4,5) -> A LIST
    for i in numbers:
        print(i)       # = 2   3   4   5
        total *= i      # se va multiplicando de a poco
    return total

print(multiply2(2,3,4,5))    # = 120

# **ARGS
def save_user(**user):
    print(user)             # = {'id': 1, 'name': john, 'age': 22} -> DICTIONARY
    print(user["name"])     # = john 

save_user(id=1, name="john", age = 22)

# SCOPE: region of the code where a variable is defined
