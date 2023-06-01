#################################################################
########## Global and Local variable  ###########################
a= 100
def functin1():
    print(f"This is from function 1: {a}")

def function2():
    a=10    #### Local variable
    print(f"This is from function 2 local variable: {a}")

def function3():
    global a
    print(f"This is from function 3 gloabl : {a}")
    a=11                    ### This will update global variable
    print(f"This is from function 3 local : {a}")
    
print(functin1())
print(function2())
print(a)
print(function3())
print(a)