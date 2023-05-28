# program to check prime number
num=int(input("enter number to check "))
if num<2:
    print ("please enter valid number")
    exit

prime=True
for i in range(2,num):
    if num%i==0:
        prime=False
        break

if prime:
    print("This number is prime")
else:
    print("This is not an prime number")


print("************* Program to check natural number *************")


# program to create sum of natural number
num2=int(input("please enter how many number you want to sum(1-9)"))
if num2<1 or num2>9:
    print("please enter valid number")
    quit()

sum=0
for i in range(1,num2+1):
    sum=sum+i

print(f"the sum of {num2} natural numbers is: {sum}")


print("************* Program to check factorial of given number *************")

num3=int(input("please enter number for which you want to see factorial"))
if num3<1 or num2>9:
    print("please enter valid number")
    quit()
factorial=1
for i in range(1,num3+1):
    factorial=factorial*i
print(f"The factorial of {num3} is: {factorial}")
