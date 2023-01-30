# Printing "Hello, World!" to the console:

print("Hello, World!")

# Taking user input and storing it in a variable:

name = input("What is your name? ")
print("Hello, " + name + "!")

# Using a for loop to iterate through a list:

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using an if-else statement to make a decision:

age = int(input("What is your age? "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Using a while loop to repeat a block of code:

count = 1
while count <= 5:
    print(count)
    count += 1

# Defining and calling a function:

def greet(name):
    print("Hello, " + name + "!")

greet("John")
greet("Mary")

    Importing and using a module:

import math

num = float(input("Enter a number: "))
print("Square root:", math.sqrt(num))

# Using a list comprehension:

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)

# Using the built-in enumerate() function to iterate through a list with index:

words = ["cat", "dog", "bird"]
for i, word in enumerate(words):
    print(i, word)

    Using a try-except block to handle exceptions:

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
