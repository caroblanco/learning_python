hermosa = "brisa"
x = "te amo"
large_string = '''
    bla bla
    bla bla
'''

#INDEX ACCESS
hermosa[0] 
hermosa[-1]     # last character of the string (a)
print(hermosa[0])

print(hermosa[0:3])     # extract a part of the string, creates a NEW string (bri)
print(hermosa[0: ])     # a copy of the original string
print(hermosa[ :3])     # assumes 0 as starting point (bri)
print(hermosa[ : ])
print(hermosa[1:-1])    # (ris)

#ESCAPE SEQUENCES   \"  \\  \n  \'
"Hola \"CARO\" "    # Hola "CARO"

#CONCAT => FORMATTED STRINGS
y = hermosa + " " + x
y2 = f"{hermosa} {x}"   # the expression in between braces will be replaced inside the string, f as in FORMATTED
ejemplo = f"{len(hermosa)} {2 + 2}"     # = "5 4"
print(y)                                # "brisa te amo"

#otro ej
first = 'Caro'
last ='Blanco'
msg = f'{first} [{last}] is a coder' # (Caro [Blanco] is a coder)

#dinamically insert values into strings

#METHODS -> EVERYTHING IN PYTHON ARE OBJECTS
#hermosa. => all the methods

len(hermosa) # cantidad de caracteres
print(len(hermosa)) #lo muestra por pantalla

print(hermosa.upper()) # NEW string with uppercases = "BRISA"
print(hermosa.lower()) # NEW string with lowercases
print(hermosa.title()) # capitalices the first letter of each word
print(hermosa.strip()) # removes white spaces at the beggining or ending of the string
print(hermosa.find("br")) # finds the first index of what you are looking for (-1 means it wasnt found)
print(hermosa.replace("b", "j")) # removes all of the first letter (or group of letters) and replaces it with the second letter (or group or letters) = "jrisa"

print("bri" in hermosa) # expression that checks if bri is in hermosa, returns a boolean = True
print("bro" not in hermosa) #expression that checks if bro is NOT in hermosa, returns a boolean = True