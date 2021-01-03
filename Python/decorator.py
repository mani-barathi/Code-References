# decorators are function which takes a function as a parameter
# and adds some functionality and then returns a another function.
# with out altering the code on the passed function 

import time
def decorator(func):
	print('inside decorator function')
	def wrapper():
		print('inside wrapper function')
		func()
		print(f"after executing {func.__name__} function")
	return wrapper

def display():
	print('display function ran')

# @decorator
# def show():
# 	print('show function ran')


# decorated_display = decorator(display)
# decorated_display()

# show()



def errorFindingDecorator(orginal_funcion):
	def wrapper(*args,**kwargs):
		value = orginal_funcion(*args,**kwargs)
		print(f'{orginal_funcion.__name__} ran with arg {args}, {kwargs} and returned {value}')
	return wrapper

def timerDecorator(orginal_funcion):
	def wrapper(*args,**kwargs):
		t1 = time.time()
		result = orginal_funcion(*args,**kwargs)
		print(f'{orginal_funcion.__name__} returned {result}')
		t2 = time.time()
		time_taken = t2 - t1
		print(f'{orginal_funcion.__name__} took {time_taken} to execute')
		return result
	return wrapper


@timerDecorator
def show():
	print('show function ran')
	time.sleep(2)


@errorFindingDecorator
def isPrime(num):
	if num == 2:
		return True
	for i in range(3,num//2+1):
		if num%i==0:
			return False
	return True

show()
isPrime(104729)
