try:
    num = int(input("Enter a number"))
    print("number is",10/num)

except ValueError:
    print("please enter a valid number")

except ZeroDivisionError:
    print("Cannot divided by zero")
