#Write a Python program to merge two lists into one dictionary using a loop.

list1 = ['id','name','city']
list2 = [18,'dhaval','rajkot']

data = {}

for i in range(len(list1)):
    data[list1[i]] = [list2[i]]

print(data)    
