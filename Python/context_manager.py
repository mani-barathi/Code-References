
# Class based implementation
class Open:
	def __init__(self,name,mode):
		self.filename = name
		self.mode = mode

	def __enter__(self):
		self.file = open(self.filename,self.mode)
		return self.file

	def __exit__(self,exc_type,exc_val,traceback):
		self.file.close()
		print("file Closed")
		if exc_type == NameError:
			print('Exception Occured:',exc_type,exc_val)
		else:
			print('Exception Occured:',exc_type,exc_val)
		return True
		

with Open('sample.txt','r') as f:
	print("file content: ",f.read())
	print(k)
print("Context manager class returned:",f.closed)

print("--------------------------------------------------------------")

# Function based implementation

from contextlib import contextmanager
@contextmanager
def openFile(file,mode):
	try:
		f = open(file,mode)
		yield f
	except Exception as e:
		print("Exception Occured:",e)
	finally:
		f.close()
		print("file closed")


with openFile('sample.txt','r') as f:
	print("file content: ",f.read())
	print(k)
print("Context manager function returned:",f.closed)
