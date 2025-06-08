def subtract_numbers(c,d):
    return c - d


def greet_user(name):
    print(f"Hello, {name}! Welcome to Python.")

def add_numbers(a,b):
    return a + b

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False
    
user_name = input("Enter your name: ")
greet_user(user_name)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum is:", add_numbers(num1, num2))

age = int(input("Enter your age: "))
if is_adult(age):
    print("You are an adult.")
else:
    print("You are not an adult yet.")