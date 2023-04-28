def f(a,x):
	return (x%18==0) <= ((x%a!=0) <= (x%12!=0))
for a in range(1,1000):
	metka = True
	for x in range(1,1000):
		if not(f(a,x)):
			metka = False
			break
	if metka == True:
		print(a)
