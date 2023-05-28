## read complete file 
a=open("file_01.txt","r")
data=a.read()
print(data+" and length is :"+str(len(data)))
a.close()

## read few characters in file 
a=open("file_01.txt","r")
data=a.read(10)
print(data+" and length is :"+str(len(data)))
a.close()

## read multiple lines in file 
a=open("file_01.txt","r")
data=a.readline() # reads first line
data=a.readline() # reads second line
print(data+" and length is :"+str(len(data)))
a.close()

## read multiple lines in file
# #  
a=open("file_01.txt","r")
data=a.readline() # reads first line
print(data+" and len is :"+str(len(data)))
data=a.readline() # reads second line
print(data+" and len is :"+str(len(data)))
a.close()


## create new file from scratch
f=open("file_02.txt","w")
f.write("This is file created by python from scractch")
f.close()

## Edit file and append new contents in file
f=open("file_02.txt","a")
f.write("\nThis is second line in file which i created earlier") # it will add this line multiple times as you will enter it here
f.close()

## using 'with' method in python for file operations, this is called as context manager also in python
## for this you dont need to explicitly close file

with open("file_03.txt","w") as f:
    a=f.write("this is third file from scratch")
    print(a)  


with open("file_03.txt") as f:  ## read file
    # a=f.write("this is third file from scratch using with method")
    a=f.read()
    print(a)  ## this will throw error as file is opened in write mode



with open("file_03.txt","a") as f:  ## append in file
    a=f.write("\nthis is new line in file through 'with' method")
with open("file_03.txt") as f:  ## read same file
    b=f.readline()  # reading first line
    print(b)  ## this will throw error as file is opened in write mode
    b=f.readline()  # reading first line
    print(b)  ## this will throw error as file is opened in write mode

############################################################################
###### Fresh assignments ###################################################
###########################################################################