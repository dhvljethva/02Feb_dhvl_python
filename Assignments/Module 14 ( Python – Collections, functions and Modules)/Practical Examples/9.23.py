# 23 Write a Python program to demonstrate the use of functions from the math module. 

import math

square = int(input("Enter a value for a square"))
print("Square root is: ",math.sqrt(square))

fact = int(input("Enter a value for a factorial"))
print("Factorial is: ",math.factorial(fact))

ceil = int(input("Enter a valur for ceil"))
print("Ceil is: ",math.ceil(ceil))

floor = int(input("Enter a value for floor"))
print("Foor is: ",math.floor(floor))

power1 = int(input("Enter a 1st number of power:"))
power2 = int(input("Enter 2nd number of power"))

print("Power is: ",math.pow(power1,power2))