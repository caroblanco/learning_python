# 1
for i in range(2,9,2):  
    print(i) 
print("we have 4 even numbers")

# -----------------------
count = 0
for i in range(1,10):
    if i % 2 == 0:
        count += 1
        print(i)
print(f"we have {count} even numbers")

# 2
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 ==0:
        return "Buzz"
    return input

print(fizz_buzz(3))
