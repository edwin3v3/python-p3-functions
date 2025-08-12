#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

greet("Jacob")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("David")

def add(num1, num2):
    return num1 + num2

print(add(1,4))
print(add(100,34))

def halve(number):
    return int(number/2)

print(halve(21.73))