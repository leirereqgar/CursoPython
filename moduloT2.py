def factorial(n):
	if n==1:
		return 1
	else:
		return n * factorial(n-1)

def esPrimo(n):
	if n<2:
		return False
	else:
		for i in range(2,n):
			if n%i == 0:
				return False
		return True
