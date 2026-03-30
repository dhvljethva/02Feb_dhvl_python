import re

mystr = "This is python"
x= re.findall("is",mystr)
print(x)

if x:
    print("match done")
else:
    print("Error")    