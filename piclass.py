
'''methods - function that is aassociated in class'''
 

class Employee:
   def __init__(self,first,last, pay):
       self.first = first
       self.last = last
       self.email = first + '.' + last + '@company.com'

   def fullname(self):
       return '{} {}'.format(self.first,self.last)

       

emp_1 = Employee('Corg','sweden',60000)
emp_2 = Employee('Test','elaiichi',70000)
emp_1.fullname()
print(Employee.fullname(emp_1))
print(emp_1.first)
print(emp_2.first)
''' Both are similar as below we are assigining manually 
    without creating init method in a class'''

emp_1.first = 'Corey'
emp_1.last = 'john'
emp_1.email = 'some@some.com'
emp_1.pay = 30000

emp_2.first = 'Test'
emp_2.last = 'sugar'
emp_2.pay = 4000