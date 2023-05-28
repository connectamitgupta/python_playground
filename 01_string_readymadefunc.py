##### function to remove spaces and replace word

def find_and_replace(strip1,strip2):
    chngstr1=strip1.replace(strip2,"")
    print (chngstr1.strip())
    
a1=input("Enter your string: ")
b1=input("Enter word you want to remove: ")
print(a1.strip())
print(b1.strip())
newa1=find_and_replace(a1,b1)