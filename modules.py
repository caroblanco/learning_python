#import another module
import functions
print(functions.get_greeting())

#import a specific function
from functions import get_greeting
get_greeting()

