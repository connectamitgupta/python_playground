#create a empty dictionary and having values inserted from user in it

favFood={}
a=input("Enter your favourite food amit:")
b=input("\nEnter your favourite food anu:")
c=input("\nEnter your favourite food devank:")
d=input("\nEnter your favourite food laviksha:")
favFood["amit"]=a
favFood["anu"]=b
favFood["devank"]=c
favFood["laviksha"]=d


print(list(favFood.items()))
print("\n")
print("favorite food for "+"is")