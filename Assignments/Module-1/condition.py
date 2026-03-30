a=int (input("Enter your gujrati mark"))
b =int (input("Enter your english mark"))
c =int  (input("Enter your math mark"))



total = a+b+c
print("total of all subject ", total)

percentage = total/3

print(percentage)

if percentage > 70:
    print("Grade +A")

elif percentage > 60:
    print("Grade A")

elif percentage > 40:
    print("Grade B")

else : 
    print("Fail")


