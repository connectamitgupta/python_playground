###############################################################################
############ OOPS program for Super Class demo ################


class persons:
    country="India"
    intro="************* Person ************"
    def takebreath(self):
        print(self.intro)
        print("I am breathing...")

class employee(persons):
    company="Honda"
    intro="************* Employee ************"
    def getsalary(self):
        pass
        #print(f"Salary is {self.salary}")
    def takebreath(self):
        #print(self.intro)
        super().takebreath()
        print("I am an employee so i am luckily breathing...")

class programmer(employee):
    company="Fiverr"
    intro="************* Programmer ************"
    def getsalary(self):
        print("No Salary to programmer")
    def takebreath(self):
        #print(self.intro)
        super().takebreath()
        print("I am a programmer so i am breathing+++...")


p=persons()
e=employee()
pr=programmer()

p.takebreath()
e.takebreath()
pr.takebreath()
