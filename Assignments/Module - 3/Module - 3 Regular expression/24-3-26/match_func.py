import re

mystr = "This is python!"

x=re.match('This',mystr)
print(x)

if x:
    print("match done")
else:
    print("error!")   