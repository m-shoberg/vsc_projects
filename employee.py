#Create class
class Employee:
    #def methods of class / how to interact w/ class
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return('{} {}'.format(self.first, self.last))
    
emp_1 = Employee("Joe", "Green", 80000)
emp_2 = Employee("Sam", "Smith", 70000)
emp_3 = Employee("Aaron", "Johnson", 60000)

print(emp_1.email)
print(emp_2.email)
print(emp_3.email)

#longer way to print full name.. see method in class
print('{} {}'.format(emp_1.first, emp_1.last))

#faster way to print full name
print(emp_1.fullname())
print(emp_2.fullname())