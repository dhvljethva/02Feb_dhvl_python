try:
     x =int(input("Enter a X:"))
     y = int(input("Enter a Y"))
     print('sum:',x+y)
except:
     print("Error")  

finally:
     print("This is always run")