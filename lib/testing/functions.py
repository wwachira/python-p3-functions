#!/usr/bin/env python3
def greet_programmer():
    #call a function
    print("Hello, programmer!")

greet_programmer()

# Function with Parameters
def greet(name):
    print(f"Hello, {name}! ")
   
greet("Guido")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# Call the function
greet_with_default("Guido")

def add(num1, num2):
    return num1 + num2

# Call the function
add(45, 55)
   
def halve(number):
    return number / 2

def halve(number):
    print(number / 2)

#call
halve(99)
halve(100)


