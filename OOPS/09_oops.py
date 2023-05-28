###################################################################################
##################################################################
class Employee:
    company="Camel"
    salary=100
    location="delhi"
    def changeSalary(self,sal):     # Simple method ##
        self.salary=sal

e=Employee()
print(Employee.salary)  ### class attribute
e.changeSalary(200) ### instance attribute change process
print(e.salary)  ### instance attribute
print(Employee.salary) ### class attribute


############ demonstrating update of class attribute through dundor class method ################
class Employee1:
    company="Camel"
    salary=100
    location="delhi"
    def changeSalary(self,sal):
        #self.salary=sal
        self.__class__.salary=sal        ### chnage class attribute from here through dundor class 

f=Employee1()
print(Employee1.salary)  ### class attribute
f.changeSalary(200) ### instance attribute change process
print(f.salary)  ### instance attribute
print(Employee1.salary) ### class attribute

############ demonstrating update of class attribute through class method ################
class Employee2:
    company="Camel"
    salary=100
    location="delhi"
    @classmethod
    def changeSalary(cls,sal):
        #self.salary=sal
        cls.salary=sal        ### chnage class attribute from here 

g=Employee2()
print(Employee2.salary)  ### class attribute
g.changeSalary(200) ### instance attribute change process
print(g.salary)  ### instance attribute
print(Employee2.salary) ### class attribute