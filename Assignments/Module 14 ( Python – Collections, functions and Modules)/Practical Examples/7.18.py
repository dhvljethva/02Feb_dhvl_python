#  18 Write a Python program to count how many times each character appears in a string.

mystr = "This is python!"
count = {}
for i in mystr:
    count[i] = mystr.count(i)

print(count)
