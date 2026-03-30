class Registration:
    def __init__(self):
        self.name = ""
        self.username = ""
        self.password = ""
        self.mobileno = ""

    def signup(self):
        self.name = input("Enter a name: ")
        self.username = input("Enter a username: ")
        self.password = input("Enter a password: ")
        self.mobileno = input("Enter a mobile number: ")
        print("Signup successfully")

    def login(self):
        if self.username == "":
            print("Please signup first!")
            return

        u = input("Enter a username: ")
        p = input("Enter a password: ")

        if u == self.username and p == self.password:
            print("Login Successfully")
            print("Welcome", self.name)
        else:
            print("Invalid username or password")


r = Registration()

while True:
    print("\n1 Signup")
    print("2 Login")
    print("3 Exit")

    ch = int(input("Enter any number: "))

    if ch == 1:
        r.signup()

    elif ch == 2:
        r.login()

    elif ch == 3:
        print("Exiting...")
        break   
    else:
        print("Invalid choice")