print ("Hello world!")
# a=6, b=3, f=10
class Class1(object): 
	def __init__(self, value):
		self.__var = value 
	def getVar(self):
		return self.__var
	def setVar(self, value):
		self.__var = value 
		
c1 = Class1(5)
print(c1.getVar())

c1.setVar(35)
print(c1.getVar())

def ingredients(func):
	def wrapper():
		print("Bread")
		func()
		print("Bread")
	return wrapper
	
@ingredient
def sandwich(food="Ham"):
	print(food)
	
sandwich()
