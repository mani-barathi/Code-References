# treat a function as a object (first class function)

# a function taking an another function as a parameter 
# or returning anotherfunction as a return value

def square(x):
	return x*x

def cube(x):
	return x*x*x

def quad(x):
	return x*x*x*x

# custom_map() is similar to map()
def custom_map(function,array):
	result = []
	for i in array:
		result.append(function(i))

	return result

arr = [1,2,3,4]
squares_array = custom_map(quad,arr)

print(squares_array)

