#Write a Python program to create a calculator using functions

num1 = int(input("Enter first Number:"))
num2 = int(input("Enter second Number:"))

def calc(num1,num2):
    print("Adition of 1st and 2nd Number is:",num1+num2)
    print("Substraction of 1st and 2nd Number is:",num1-num2)
    print("Multiplicatiom of 1st and 2nd Number is:",num1*num2)
    print("devision of 1st and 2nd Number is:",num1/num2)
    print("Modulus of 1st and 2nd Number is:",num1%num2)

calc(num1,num2)