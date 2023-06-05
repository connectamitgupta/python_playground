# a = [1, 2, 3, 4] 
# b = [5, 6, 7, 8] 
# c = [] 
 
# for i in range(len(a)): 
#     c.append(a[i] + b[i]) 
 
# print(c) 


##############################################

from ctypes import c_int, addressof
  
# get memory address of variable
a = 44
b=[]
print(addressof(c_int(a)))
print(id(a))

print(id(a) + CDataObject.b_value.offset)
#print(addressof(c_int(b)))