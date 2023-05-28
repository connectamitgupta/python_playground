a=input("enter number 1: ")
b=input("enter number 2: ")
if (a<b):
    print("a is less than B")
else:
  print("A is greater than b")

print("--------------------------------------")
s=input("enter your name: ")
age=int(input("enter your age: "))

if (age>30 and age<40):
   print("You are fit for this job")
else:
   print("You are not fit for this job") 


print("--------------------------------------")
# check how 'None' with 'is' works here
c=None
if (c is None):
   print("Yes, c is none and checked")
else:
   print("c is not none")