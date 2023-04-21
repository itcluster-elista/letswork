class Calculator:
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
	
	def plus(self):
		print(self.num1 + self.num2)
	
	def minus(self):
		print(self.num1 - self.num2)
	
	def mult(self):
		print(self.num1 * self.num2)
	
	def divide(self):
		print(self.num1 / self.num2)

ob1 = Calculator(40, 20)

ob1.plus()

ob1.minus()

ob1.mult()

ob1.divide()
