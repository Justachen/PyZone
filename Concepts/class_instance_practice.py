import datetime


class Employee:

	num_of_emps = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
		
	# Class Methods
	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	# Class Method that is used as a constructor
	@classmethod
	def from_string(cls, emp_string):
		first, last, pay = emp_string.split('-')
		return cls(first, last, pay)

	# Static Methods
	# Sign to use static method, when you create a method that doens't need to access either the class or self Vars
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

	def __str__(self):
		return '{} - {}'.format(self.fullname(), self.email)

class Developer(Employee):

	raise_amount = 1.1

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

class Manager(Employee):

	def __init__(self, first, last, pay, employees = None):
		super().__init__(first, last, pay)
		if employees == None:
			self.employees = []
		else:
			self.employees = employees

	def add_employee(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_employee(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_employees(self):
		for emp in self.employees:
			print('-->', emp.fullname())


emp_1 = Employee('Justin', 'Chen', 50000)
emp_2 = Employee('Test', 'User', 60000)
emp_3 = Employee('Jack', 'Snow', 100000)

emp_string1 = 'Dogs-Cats-10'
emp_4 = Employee.from_string(emp_string1)

dev_1 = Developer('Corey', 'Schafer', 100000, 'Python')

mang_1 = Manager('Steph', 'Rodrigez', 1000000)

# print(mang_1.fullname())
# print(mang_1.email)
# mang_1.add_employee(emp_1)
# mang_1.add_employee(emp_2)
# mang_1.add_employee(emp_3)
# mang_1.add_employee(dev_1)
# mang_1.print_employees()
# mang_1.remove_employee(emp_1)
# mang_1.print_employees()

# print(issubclass(Manager, Employee))

print(str(emp_1))
