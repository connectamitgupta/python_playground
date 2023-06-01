######################################################################
######## Learn Comprehensions in python ##############################

a=[1,4,7,9,4,6,7,3,8]
b=[]
for i in a:
    if i%2==0:
        b.append(i)
print(b)

#### through comprehension method

x=[17,27,48,54,87,45,34,90,22,10]
y=[]

y=[i for i in x if i%2==0]

print(y)
