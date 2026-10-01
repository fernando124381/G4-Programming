"""
Filename: condicional_calculator.py
Author: <Tinoco, Fernando>
Created: <09/29/2026>
Instructor: Burgess
"""

print ("Hello, here is a condicional calculator featuring multiplication, division, addition, and subtraction.")

number1 = int(input("And now, please enter a number, this is the first number ( '0' +X).   "))

symbol1 = input("Which operation do you want to enter? These are the signs for the operations (addition + \n, subtraction -, multiplication *, or division /   ")

number2 = int(input("And again, please enter a number, this is the second number (X+ '0' ).    "))


if symbol1 == "+":
    print(f"{number1} + {number2} = {number1 + number2}")

elif symbol1 == "-":
    print(f"{number1} - {number2} = {number1 - number2}")

elif symbol1 == "*":
    print(f"{number1} * {number2} = {number1 * number2}")

elif symbol1 == "/":
    print(f"{number1} / {number2} = {number1 / number2}")




