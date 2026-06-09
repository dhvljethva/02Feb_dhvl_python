#Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue
#statement. List1 = ['apple', 'banana', 'mango']

list1 = ['apple','banana','mango']
for list1 in list1:
    if list1 == "banana":
        continue
    print(list1)
