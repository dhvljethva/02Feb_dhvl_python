data = {}
n = int(input("How many items: "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

print(data)