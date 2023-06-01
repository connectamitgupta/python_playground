def addition(i,j):
    return i+j

def substraction(i,j):
    if i>j:
        return i-j
    else:
        return j-i

if __name__=="__main__":    ### The purpose of using this dundor class here to stop unwanted code execution when this file being called from other file. 
    print(addition(4,5))
    x=input("Enter first number: ")
    y=input("Enter second number: ")
    try:
        print(f"Result is here: {addition(int(x),int(y))}")
    except Exception as e:
        print(f"There is some input error by you so exiting automatically: \n {e}")
    else:
        print("Success! You run this program again")