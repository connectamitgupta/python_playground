###############################################################################
############ OOPS program for class inheritance demo ################
## 1### for multiple inheritance ####

# class employee:
#     company="jumbo"

# class freelancer:
#     company="none"
#     level=0

#     def upgradeLevel(self):
#         self.level=self.level+1

# class programmer(employee,freelancer):      ## Multiple inheritance is here
#     name="rohit"


# p=programmer()
# print(p.name)
# p.upgradeLevel()
# print(p.level)



############ OOPS program for class inheritance demo ################
## 1#######


## 2### for multi Level inheritance ####


class persons:
    country="India"
    def takebreath(self):
        print("I am breathing...")

class employee(persons):
    company="Honda"
    def getsalary(self):
        pass
        #print(f"Salary is {self.salary}")
    def takebreath(self):
        print("I am an eployee so i am luckily breathing...")

class programmer(employee):
    company="Fiverr"
    def getsalary(self):
        print("No Salary to programmer")
    def takebreath(self):
        print("I am a programmer so i am breathing+++...")


p=persons()
e=employee()
pr=programmer()

pr.getsalary()
pr.takebreath()

e.getsalary()