import random
import os
############################################################################
###### Fresh assignments ###################################################
############################################################################
#1  # writing a poem in a file  ######################

f=open("twinkle_poem.txt","w")
f.write("Twinkle tinkle little star \n\t how are wonder what youa are\n\t up above the world is so high\n\t like a diamond in the sky")
f.close()

#1  # searching text in file (normal which is case sensitive) ######################
srch=input("Enter text which you want to search: ")
with open("twinkle_poem.txt") as x:
    f=x.read()
    if srch in f:
        print(f"Entered text {srch.upper()} exists in file")
    else:
        print("text does not exists in file")


#1  # searching text in file (now case insensitive) ######################
srch=input("Enter text which you want to search: ")
with open("twinkle_poem.txt") as x:
    f=x.read()
    f1=f.upper()
    if srch.upper() in f1:
        print(f"Entered text {srch.upper()} exists in file")
    else:
        print("text does not exists in file")

###################################################################################
#2  # find value and compare text in file ######################

def game():
    return random.randint(50,100)

with open("gamescore.txt") as f:
        oldscore=f.read()
        if len(oldscore)==0:
            score=int(input("Enter your number to your chance: "))
            oldscore=0
        else:
            score=oldscore
            print(f"previous score already exists in file which is {score}")

gamescore=game()
print("Computer generated number is : "+str(gamescore))

if int(oldscore)==gamescore:
    print("Both score are same so no need to update file")
elif int(oldscore)>gamescore:
    print("No need to update in file")
elif int(score)>gamescore:
    with open("gamescore.txt","w") as f:
        x=f.write(str(score))
    with open("gamescore.txt") as f:
        x=f.read()
        print(f"This value {score} have been updated in file")
else:
    with open("gamescore.txt","w") as f:
        x=f.write(str(gamescore))
    with open("gamescore.txt") as f:
        x=f.read()
        print(f"This value {gamescore} have been updated in file")

###################################################################################
##3  # Generate multiple files for tables #########################################
print("************* Table generation in seperate files ***********************")
i=int(input("Enter FROM number: "))
j=int(input("Enter TO number: "))+1
os.mkdir("assignment_table")    ## generate a folder using os module
for i in range(i,j):
    with open(f"assignment_table\\table of {i}.txt","w") as f:
        for k in range(1,11):
            f.write(f"{i}x{k}={i*k}")
            if k!=10:
                f.write(f"\n")


###################################################################################
##4  # Program to search text in large file  #########################################
print("************* Program to search text in large file ***********************")
content= True
searchstring=input("Enter text to search")
with open("log.txt") as f:
#    content=f.read()
    i=0
    while content:
        content=f.readline()
        if searchstring in content:
            print(f"Enetered text {searchstring.upper()} exists in file at {i+1}")
        i+=1
        

###################################################################################
##4  # Program to show file information  #########################################

with open("log.txt") as f:
    print("filename is: ",f.name)   ## using os module which is imported on top
    print("File open mode is ",f.mode)  ## using os module which is imported on top
    print("File open or closed ",f.closed)  ## using os module which is imported on top

check=input("do you want to remove directory genrated for assigment table: y/n ")
if check=='y':
    os.rmdir("assignment_table")
    print("directory deleted successfully")
else:
    print("directory not deleted")
