import random

### creating Snack, Water and Gun game

def gameWin(comp,you):
    pass
    if comp==you:
        print("This match is tie")
    elif comp=='s':
        if you=='w':
            print("You lost")
        elif you=='g':
            print("You won")
    elif comp=='w':
        if you=='s':
            print("You Won")
        elif you=='g':
            print("You lost")
    elif comp=='g':
        if you=='s':
            print("You lost")
        elif you=='w':
            print("You won")


print("Its computer turn: Snake(S), Water(W), Gun(G)")
print("Wait...computer is choosing")
randNo=random.randint(1,3)   ## its for computer's selection

you=input("Please select Snake(S), Water(W), Gun(G) : ")


if randNo==1:
    comp='s'
    comstring="Snake"
elif randNo==2:
    comp="w"
    comstring="Water"
elif randNo==3:
    comp="g"
    comstring="Gun"

if you=='s':
    youstring="Snake"
elif you=='w':
    youstring="Water"
elif you=='g':
    youstring="Gun"

print(f"Computer have chosen {comstring.upper()} and You have chosen {youstring.upper()}")
x=gameWin(comp,you)