marks =int(input("Enter your marks"))

if(marks>=90):
    grade = "A"

elif(marks>=80 and marks<90):
    grade = "B"

elif(marks>=70 and marks<80):
    grade = "C"

else:
    grade = "D"

print("Your grade",grade)


### TASK ###

num = int(input("Enter any number"))
rem = num % 2

if(rem == 0):
    print("EVEN")
else:
    print("ODD")

