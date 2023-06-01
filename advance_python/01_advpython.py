########################## Learning advanced python ###########################
################ Using TRY and CATCH statement to handle error ###############
while(True):
    print("Press enter Q to quit")
    a=input("Please enter number to play this game; ")
    if a=='q':
        break
    try:
        a=int(a)
        if a>6:
            print("Entered number is greater than 6")
        else:
            print("Entered number is less than 6")
    except Exception as e:
        print(e)
print("Thanks for playing fair")