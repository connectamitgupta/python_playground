########################## Learning advanced python ###########################
####### Using TRY/CATCH with ELSE statement  ########################
while(True):
        a=input("Enter any number to increase its value: ")
        
        if a=='q':
            break
        try:
            a=int(a)
            a+=1
            print(a)

        except Exception as e:
            print(f"There is some isssue: {e}")
        else:               ### this will be executed in case of exception is not met
             print("  We are done!")
       
#print("Thanks for playing fair")