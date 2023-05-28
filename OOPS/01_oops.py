####################### object oriendted programming ########################
#### class creation to understand first time ###########################
class employee:
    company="trevita"
    def info(self):
        return "This is employee named class"
    def ageprint(self):
        print(f"{self.name} age is {self.age}")

amit=employee()
sumit=employee()
print(amit.company)  ### this will print class attribute becasue their is instance/object attribute is defined yet
amit.name="amit"
amit.age=40
sumit.age=35
print(amit.name)  ### this will print instance/object attribute which is defined through vaiable
print(amit.age)   ### this will print instance/object attribute which is defined through vaiable
print(amit.info())  ### printing class attribute
print(sumit.info()) ### printing class attribute
##print(amit.address)   ### this will throw an error as their no instance/ class attribute
sumit.name="sumit"
sumit.ageprint()