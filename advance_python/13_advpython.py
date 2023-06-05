########################################################################################################
################## Using LAMBDA function ####and use of JOIN function also #############################
########################## The lambda function sometime is used as an arguments in function calls ###### 
########### Lambda is noting, its just convenience for programming #####################################
######### Lambda is called as Ananymous function also ##################################################
test1=lambda a:a+5
print(test1(5))

print("*"*50)

test2=lambda x,y,z:x+y+z+8
print(test2(2,3,4))

test3=lambda p:print(f"{p} is good boy")

print(test3("ram"))
################################ Demonstration of JOIN function in Python ####################################

a=["banana","mango","papaya","cherry"]              ## This is an List
print(" and ".join(a))

b=("banana","mango","papaya","cherry")              ### This is an tuple
print(" and ".join(b))

################################### Use of FORMAT instead of fstring method ##################################

name="Kapil"
age=67
city="Jaipur"

print(f" Your name is {name} and age is {age} and city is {city}")

print(" Your name is {} and age is {} and city is {}".format(name,age,city))

print(" Your city is {2} and age is {1} and name is {0}".format(name,age,city))


