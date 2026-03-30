f1 = open('temp.txt','a')

data = int(input("How many data you store in file!"))
for i in range(data):
    id = input("Enter your ID:")
    name = input("Enter your name:")

    f1.write(f"ID:{id}\n")
    f1.write(f"Name:{name}\n")    

f1.close