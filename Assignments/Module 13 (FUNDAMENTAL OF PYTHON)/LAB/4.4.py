#Practical Example 8: Write a Python program to check if a person is eligible to donate blood
#using a nested if.

age = int(input("Enter your age"))
blood = input("Enter your blood group")

if age > 18:
    if blood == "A+":
        print("Your are eligible to donate a blood")

    elif blood == "A-":
        print("Your are eligible to donate a blood")

    elif blood == "B+":
        print("You are eligible to donate a blood") 

    elif blood == "B-":
        print("You are eligible to donate a blood")

    elif blood == "O+":
        print("You are eligible to donate a blood")

    elif blood == "O-": 
          print("You are eligible to donate a blood")  

    else:
          print("Invalid blood group") 

else:
     print("YOu are not eligible to donate ablood")
