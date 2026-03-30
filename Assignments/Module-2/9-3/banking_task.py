def bankdata(AcNumber, Acname, Actype):
    print("Your account number:", AcNumber)
    print("Your account name:", Acname)
    print("Your account type:", Actype)

num1 = int(input("Enter your account number: "))
num2 = input("Enter your account name: ")
num3 = input("Enter your account type: ")

bankdata(num1, num2, num3)

balance = 0

def deposit(balance, depo):
    if depo > 2000:
        balance = balance + depo
        print("Amount deposited")
        print("Your current balance:", balance)
    else:
        print("Minimum amount must be 2000!")
    return balance

n = int(input("Enter amount to deposit: "))
balance = deposit(balance, n)

def withdraw(balance, withd):
    if withd < balance:
        balance = balance - withd
        print("Your current balance:", balance)
    else:
        print("Insufficient balance:", balance)
    return balance

wd = int(input("Enter amount to withdraw: "))
balance = withdraw(balance, wd)

def statement(balance):
    print("\n--- Account Statement ---")
    print("Account number:", num1)
    print("Account name:", num2)
    print("Account type:", num3)
    print("Account balance:", balance)

statement(balance)