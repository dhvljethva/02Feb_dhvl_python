name = input("Enter your name")
with open("demo.txt","w") as file:
    file.write(name)

print("Name saved successfully!")    