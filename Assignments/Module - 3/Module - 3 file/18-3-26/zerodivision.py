try:
    x = int(input("Enter any number:"))
    print(10/x)

except ZeroDivisionError:
    print("cannot divide by zero!")

except:
    print("invalid input")    
   