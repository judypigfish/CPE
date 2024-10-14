while 1:
	n = int(input())
	if n == 0:
		break
		
	s = set()
	while n not in s:
		s.add(int(n))
		n **= 2
		n //= 100
		n %= 10000
	
	print(len(s))
