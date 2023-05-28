# check how 'None' with 'is' works here
c=None
if (c is None):
   print("Yes, c is none and checked")
else:
   print("c is not none")

print("--------------------------------------")

d=[2,3,4,5,6]
inp1=int(input("Enter value to check"))
#print(inp1 in d)
if (inp1 in d):
   print("This number exists in list")
else:
   print("This number does not exists in list")