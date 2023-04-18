num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

if num2 > num1:
	num1, num2 = num2, num1

print(num1, num2)
