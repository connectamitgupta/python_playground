##########################################################################
############# Enumerate fuunction ########################################
######### 
car=["maruti",80000,"BS IV", 2015]
x=0
for i in car:
    print(f"This is traditional method: {x}, {i}")
    x+=1

for index, item in enumerate(car):              ### using enumerate function, code become very short
    print(index,item)

    