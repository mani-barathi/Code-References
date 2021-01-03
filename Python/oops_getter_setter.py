class Employee:
	raise_amt = 1.05
	def __init__(self,fname,lname,pay):
		self.first = fname
		self.last = lname
		self.pay = pay
		
	@property	
	def fullname(self):
		return f'{self.first} {self.last}'

	@property
	def email(self):
		return f'{self.first}{self.last}@school.com'.lower()	

	@fullname.setter
	def fullname(self,name):
		self.first, self.last = name.split(' ')

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)


s = Employee('Mani','barathi',2000)

print(s.fullname)
print(s.email)

print('-----------')

s.fullname = 'Manibharathi S'
print(s.fullname)
print(s.email)