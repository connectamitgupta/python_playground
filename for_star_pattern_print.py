# program to print "*" for number of times
print("*"*40)
#num=int(input("enter number of rows for *"))
num=6
for i in range(num):
    print("*"*(i+1))
print("\n\n Now see new star ")
# program to print "*" for number of times
for i in range(num):
    print(" "*(num-i),end="")
    print("*"*(i+1),end="")
    print(" "*(num-i))
    
# program to print square using "*" for number of times

for i in range(1,num+1):
    if(i==1 or i==num):
        print("*"*num)
    else:
        print("*",end="")
        print(" "*(num-2),end="")
        print("*")
