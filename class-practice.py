class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + last + "@company.com"

emp_1 = Employee("Minhal", "Sami", 90000)
emp_2 = Employee("Someone", "Last", 50000)

print(emp_1.email)
print(emp_2.email)