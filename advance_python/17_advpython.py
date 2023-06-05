###########################################################################################
########### Practice set
from functools import reduce

def table(num):
    for i in range(1, 11):
        print(i * num)


print(table(10))

k = [str(i * 10) for i in range(1, 11)]
print(k)

vtable = "\n".join(k)

print(vtable)

############################################################################################################
#################### List filter which number are divisible by 5 ###########################################
ln = [2, 5, 7, 9, 13, 15, 24, 35, 90, 456, 345]
lnfunc = lambda num: num % 5 == 0

print(list(filter(lnfunc, ln)))

############################################################################################################
#################### Use reduce function to find out maximum from a list  ###########################################

kk=[34,67,89,32,19,21,23]

a=reduce(max,kk)
print(a)
a1=reduce(min,kk)
print(a1)
