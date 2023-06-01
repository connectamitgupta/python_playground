########################## Learning advanced python ###########################
####### Using TRY and CATCH using customised handling error ###############
while(True):
        a=input("Enter any number to increase its value: ")
        
        if a=='q':
            break
        try:
            a=int(a)
            a+=1
            print(a)

        except:
             raise ValueError("This is very bad input dear user")

print("Thanks for playing fair")