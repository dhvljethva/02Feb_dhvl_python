import re
mystr = "That is python!2345676"
#x = re.findall("^This",mystr)
x = re.findall('^[A-Z]',mystr)
print(x)