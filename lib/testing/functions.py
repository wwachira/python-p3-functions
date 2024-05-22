#!/usr/bin/env python3
def greet_programmer():
    #call a function
    print("Hello, programmer!")

greet_programmer()

# Function with Parameters
def greet(name):
    print(f"Hello programmer {name} ")
   

greet("Liz")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# Call the function
greet_with_default()

def add(num1, num2):
    print(f"{num1 + num2}")

# Call the function
add(45, 55)
   
def halve(number):
    print(number / 2)

#call
halve(100)