####################################################################################################
######## FILTER and REDUCE function ###########################################################################
def greter_then_5(num):
    if num>5:
        return True
    else:
        return False
    
g10=lambda num: num>10                          ### Use of Lambda function

l=[1,2,3,5,10,25,47,72,89,100]
print(list(filter(greter_then_5,l)))           ### Filter using Normal function
print(list(filter(g10,l)))                     ### Filter using Lambda function
