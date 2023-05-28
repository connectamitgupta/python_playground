class fruits:
    company="Microsoft"
    def nameinfo(self):
        print(f"Fruit name is {self.colorinfo().name}")
        
    def fruitinfo(self):
        #dt=self.dob
        if self.ask=='A':
            name="apple"
            color="red"
        elif self.ask =='O':
            name ='orange'
            color="orange"
        elif self.ask=='M':
            name="mango"
            color='yellow'
        elif self.ask=='C':
            name="Chikoo"
            color='Brown'
        else:
            print("Not an vaid input provided")
            exit()    
        print(f"Fruit name is {name} and color is {color}")

fruits1=fruits()
fruits2=fruits()
fruitdictionary={"Orange":"O","Mango":"M","Chikoo":"C","Exit":"E"}

fruits1.ask=input(f"{list(fruitdictionary.items())} \n Enter fruit name: ").upper()
fruits2.ask=input(f"{list(fruitdictionary.items())} \n Enter fruit name: ").upper()

if fruits1.ask not in fruitdictionary.values():
    exit()

if fruits2.ask not in fruitdictionary.values():
    exit()

fruits1.fruitinfo()
fruits2.fruitinfo()
