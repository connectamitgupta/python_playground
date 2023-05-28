###################################################################################
######## Getter setter methods ####################################################
###################################################################################
class Employee:
    company="Bharat Gas"
    salary=4000
    salaryBonus=400
    #totalSalary=4500
    @property               #### defining attribute through property method and it is called Getter method also.
    def totalSalary(self):
        return self.salary+self.salaryBonus
  
    @totalSalary.setter         ### applied Setter method here to change value
    def totalSalary(self,val):
        self.salaryBonus=val-self.salary

e=Employee()
print(e.salary)
print(e.salaryBonus)
print(e.totalSalary)
e.totalSalary=7000                  # now using getter method here to dynamic updates in attributes
print(e.salary)
print(e.salaryBonus)
print(e.totalSalary)
