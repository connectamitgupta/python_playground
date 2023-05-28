a=int(input("Please enter no of row "))
b=int(input("Please enter no of column"))

i=0
while (i<a):
    print("*")
    i +=1    

# create a table through for loop

num= int(input("Please enter number for which you want to create table"))

for i in range(1,11):
    print(str(i)+" value is :"+str(i*num))

# using fstring in expression
num2=int(input("Enter number to create table"))
print(f"printing table of {num2}")
for j in range (1,11):
    print(f"{j}th value for {num2} is : {j*num2}")

# using prebuilt functions with for loop
li=["ram","rajesh","mohan","ajay","vijay"]
print(list(li))
ch=input("please enter character through you want to search")
for i in li:
    if i.startswith(ch):
        print(f"Hello {i}")

p=0
while p<=10:
    print(f"table of {num2} and {p} is: {p*num2}")
    p+=1
    