########################################################################################################
########## Use of Map function in python #########################################################
############## Map applies function to all item in a list #################################
### Demo1 through traditional method
def square(num):
    return num*num

li1=[1,2,3,5,8]
li2=[]
for item in li1:
    li2.append(square(item))
print(li2)


#### Using MAP method
li3=[1,2,3,5,8]
print(f"Generate  Squared using MAP method: {list(map(square,li3))}")       ## After applying MAP function, used list function to typecast output

def roor(num2):
    if num2%2==0:
        return True

li4=[1,2,3,5,8]
print(f"Check PRIME number throgh MAP method: {list(map(roor,li4))}")
print(f"Check PRIME number throgh MAP method and Apply FILTER: {list(filter(roor,li4))}")
