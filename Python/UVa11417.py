def gcd(a,b):
	if b == 0:
		return a
	return gcd(b,a%b)

while 1:
	a = int(input())
	if a == 0:
		break
		
	G = 0
	for i in range(1,a):
		for j in range(i+1,a+1):
			G += gcd(i,j)
	print(G)
	
