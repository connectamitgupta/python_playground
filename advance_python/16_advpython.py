####################################################################################################
######## REDUCE function ###########################################################################
from functools import reduce

sum1=lambda num1,num2: num1+num2                          ### Use of Lambda function
multiply1=lambda num3,num4: num3*num4

l=[1,2,3,5,10,25,47,72,89,100]
#print(list(filter(greter_then_5,l)))           ### Filter using Normal function
print(reduce(sum1,l))                     ### Filter using Lambda function
print(reduce(multiply1,l))                     ### Filter using Lambda function