citie = ["Rajkot","vadodara","surat","junagadh"]

def print_length(list):
    print(len(citie))

print_length(citie)
print(citie[0],end=" ")
print(citie[1])
 


#==================

def calculate(n):
    factorial = 1
    for i in range(1,n+1):

     factorial *= i
    print(factorial)

calculate(5)  


#==================

def calculate(usd_val):
   inr_val = usd_val * 83
   print(usd_val,"USD=",inr_val,"INR")

calculate(34)
