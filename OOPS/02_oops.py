class staff:
    company="Microsoft"
    def salaryinfo(self):
        print(f"Salary is {self.salary}")
        #return "Salary is: "

    def ageinfo(self):
        #dt=self.dob
        age=2023-1990
        print(f"Age is: {age}")

amit= staff()
amit.name="amit"
amit.salary="50000"
print(amit.name)
print(amit.salary)
amit.salaryinfo()
amit.ageinfo()