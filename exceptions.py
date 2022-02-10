try:
    age = int(input("Age: "))
    print(age)
except ValueError:              #conversion error
    print("Invalid value")
except ZeroDivisionError:       #cuando dividis por cero
    print("No seas tonto")