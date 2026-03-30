import re

mystr = "That is python!"      

x= re.search('python',mystr)  
print(x)

if x:
    print("match done")

else:
    print("error!")