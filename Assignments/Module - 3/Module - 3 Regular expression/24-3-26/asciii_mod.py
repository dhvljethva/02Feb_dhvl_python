import re
mystrt = "This is Python!456778"

#x = re.findall('\w',mystrt)
#x = re.findall('\W',mystrt)
#x = re.findall(R'\bThis',mystrt)
#x = re.findall('\B78',mystrt)
#x = re.findall('\s',mystrt)
#x = re.findall('\S',mystrt)
x = re.findall('\d',mystrt)

print(x)
