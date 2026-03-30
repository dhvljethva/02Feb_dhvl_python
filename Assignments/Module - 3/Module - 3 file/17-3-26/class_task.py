import datetime
import random

n = int(input("Number of student: "))
now = datetime.datetime.now()
for i in range(n):
    num = random.randint(1,10)
    
    print(now.strftime("%Y-%m-%d")) #date
    print(now.strftime("%H:%M:%S"))    #time
    print(num)
    
    name = input("Enter your name:")
    city = input("Enter your city")


