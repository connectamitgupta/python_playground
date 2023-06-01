########################## Learning advanced python ###########################
####### Using TRY and CATCH different statement to handle error ###############
while(True):
        a=input("Enter any number: ")
        
        if a=='q':
            break
        try:
            a=int(a)
            p=1/a
            print(p)

        except BaseException as b:
            print(f"Please enter correct number: {b}")
        except ZeroDivisionError as b:
            print(f"Zero division error: {b}")
        except ValueError as b:
             print(f"There is value error occured: {b}")

print("Thanks for playing fair")