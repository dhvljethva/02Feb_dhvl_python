import re
class Signup():
 def getdata(self):
  print("-----SIGNUP FORM----- ")

  firstname = input("Enter your name: ")
  self.lastname = input("Enter your lastname: ")
  self.email = input("Enter your email: ")
  self.password = input("Enter your password: ")
  self.confirm = input("confirm password: ")
  self.mobileno = input("Enter your mobile number: ")
  
  fn_patter = "^[A-Z]+[a-z]+$"
  ln_patter = "^[A-Z]+[a-z]+$"
  en_patter = "^[a-z0-9]+[@]+[a-z]+[\.]+[a-z]"
  pn_patter = "^[A-Z]+[a-z]+[0-9]+$"
  cn_patter = "^[A-Z]+[a-z]+[0-9]+$"
  mn_patter = "^[0-9]+$"


  x = re.match(fn_patter,firstname)
  l  = re.match(ln_patter,self.lastname)
  e = re.match(en_patter,self.email)
  p = re.match(pn_patter,self.password)
  c = re.match(cn_patter,self.confirm)
  m = re.match(mn_patter,self.mobileno)

  print("---VALIDATION RESULT---")


  if x:
   print('Your Firtname is valid.')
  else:
   print('Error! First name is invalid..') 

  if l:
    print('Your Last name is valid.')
  else:
    print('Error! Last name is invalid..') 

  if e:
   print('Your email is valid.')
  else:
   print('Error! Your email is invalid..')

  if p:
   print('Your Password is valid.')
  else:
   print('Error! Password is invalid..')

  if c:
   print('Confirm Password is valid.')
  else:
   print('Error! Password is invalid..')

  if self.password == self.confirm:
   print('Your Password is match.')
  else:
   print('Error! Password is not match..') 


  if m:
   print('Your Mobile number is valid!')
  else:
   print('Error! Mobile number is invalid!') 
 
s=Signup()
s.getdata()


  
 