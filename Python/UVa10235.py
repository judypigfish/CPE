while 1:
	try:
		n = int(input())
	except:
		break
	
	def p(num):
		for i in range(2, int(num**0.5)+1):
			if num % i == 0:
				return False
		return True
	
	if p(n):
		if p(int(str(n)[::-1])) and n > 10 and str(n) != str(n)[::-1]:
			print(f"{n} is emirp.")
		else:
			print(f"{n} is prime.")
	else:
		print(f"{n} is not prime.")
