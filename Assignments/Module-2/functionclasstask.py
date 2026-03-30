def bankdata(AcNumber, Acname, Actype):
    print("Your accout number",AcNumber)
    print("Your account name: ",Acname)
    print("Your accout type: ",Actype)

num1 = int(input("Enter your account number"))
num2  = (input("enter your Account name"))
num3  = (input("Enter your account type"))  
    
bankdata(num1,num2,num3)

balance= 0
def deposit(depo):
    if n > 2000:
        global balance
        balance=balance+n
        print("Amount deposit \n Your current balance",balance)
    else:
        print("Minimum Amount must be 2000!")    
n = (int(input("Enter a amount of deposit")))

deposit(n)

def withdraw(withd):
    global balance
    if wd < balance:
       balance = balance - wd
       print("our current balance",balance)

    else:
        print("Insufficient Balance",balance)

wd = int(input("Enter amount "))
   
withdraw(wd)   

def statement():
    print("Your account number: ",num1)
    print("Your account name: ",num2)
    print("Your account type: ",num3)
    print("Your account balance",balance)

statement()    



      
