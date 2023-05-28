import math

class Areacalc:
    title="********* This is Maths calculator ****************"
    def __init__(self,num):
        print(self.title)
        self.number=num
    def sqrt(self):
        print (f"Squareroot of {self.number} through math library is : {math.sqrt(self.number)}")
        print (f"Squareroot of {self.number} through classical method is: {self.number**0.5}")

    def cube(self):
        print(f"Cubical of {self.number} is {self.number**3}")
    def square(self):
        print(f"Square of {self.number} is {self.number**2}")

x=int(input("Enter number for which you want to calulate(Root, Cube and Square)"))
calc1=Areacalc(x)
calc1.square()
calc1.cube()
calc1.sqrt()