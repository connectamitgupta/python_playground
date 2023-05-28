### functions ################################################################
## perccentage wwithout function ##############################

marks1=[55,98,67,45]
marks2=[63,98,91,71]
marks3=[67,56,98,77]
marks4=[88,69,67,87]

percent1= ((marks1[0]+marks1[1]+marks1[2]+marks1[3])/400)*100
percent2= ((marks2[0]+marks2[1]+marks2[2]+marks2[3])/400)*100

percent3= (sum(marks3)/400)*100
percent4= (sum(marks4)/400)*100
print("This is using simple method to calculate percentage")
print(percent1,percent2,percent3,percent4)

## perccentage using function ##############################

def percentage(marks):
    p=((sum(marks)/400)*100)
    return p
print("This is using function to calculate percentage")
print(percentage(marks1),percentage(marks2),percentage(marks3),percentage(marks4))


## greetings using function ##############################

def greeting(name):
    print(f"hello {name}!,welcome to learning program")
    #print(f"today is {now()}")

a=input("Please enter your name for greetings :")
greeting(a)


## Recursion using function ##############################

def factorial(fac1):
    if fac1==0 or fac1==1:
        return 1
    fac2=fac1*factorial(fac1-1)
    return (fac2)

fac1=int(input("Please enter number to find factorial:"))
print(factorial(fac1))