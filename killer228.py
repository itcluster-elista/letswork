while True:
	x = input()
	compiled_str = compile(x, 'string', 'eval')
	print(eval(compiled_str))
