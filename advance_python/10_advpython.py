#####################################################################
########### Verify file exists or not and handle through exception ##

def fileread(filename):
    try:
        with open(filename,"+r") as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f"File {filename} is not found")

fileread("advance_python/01_advpython.py")
fileread("advpython.py")