class registation:

    def sigup(self):
        name = input("Enter your name: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        mobileno = input("Enter your mobile number: ")
        
        return name, username, password, mobileno

    def login(self, stored_username, stored_password):
        u = input("Enter your username: ")
        p = input("Enter your password: ")

        if u == stored_username and p == stored_password:
            print("Login Successfully")    
            print("Welcome", stored_username)  
        else:
            print("Invalid username or password")


obj = registation()

username = ""
password = ""

while True:
    print("\n1 Signup")
    print("2 Login")
    print("3 Exit")

    ch = int(input("Enter number: "))

    if ch == 1:
        obj.sigup()

    elif ch == 2:
        obj.login()

    elif ch == 3:
        print("Exiting...")
        break

    else:
        print("Invalid Choice") 








