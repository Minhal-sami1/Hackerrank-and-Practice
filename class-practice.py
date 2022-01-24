class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + last + "@company.com"
class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

emp_1 = Developer("Minhal", "Sami", 90000, "Python")
emp_2 = Employee("Someone", "Last", 50000)

print(emp_1.first, emp_1.last)
print(emp_1.prog_lang)