class Product:
	def __init__(self,name,price):
		self.__name = name
		self.__price = price
	
	def base_info(self):
		print(f"""
		name: {self.__name}
		Price: {self.__price}
		""")


class Desktop(Product):
	def get_info(self,pc,videocard, hdd):
		self.__pc = pc
		self.__videocard = videocard
		self.__hdd = hdd
	def about_product(self):
		self.base_info()
		print(f"""
		Processor: {self.__pc}
		Videocard: {self.__videocard}
		hdd: {self.__hdd}
		""")

class Smartphone(Product):
	def get_info(self, os, memcard, camera):
		self.__os = os
		self.__memcard = memcard
		self.__camera = camera
		
	def about_product(self):
		self.base_info()
		print(f"""
		os = {self.__os}
		memcard = {self.__memcard}
		camera = {self.__camera}
		""")

def show_info(obj):
	obj.about_product()
	
d1 = Desktop("Acer", 80000)
d1.get_info("Intel icore", "Gforce", "Kingston")

s1 = Smartphone("Honor", 20000)
s1.get_info("Android", "Lexar", "AI Camera")

show_info(d1)
show_info(s1)
