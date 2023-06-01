########################## Learning advanced python ###########################
####### Using finally statement in TRY/CATCH statement  ########################
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
            exit()
        finally:            ### this will be executed regardless of error
             print(" We are done!")
       
print("Thanks for using this program")