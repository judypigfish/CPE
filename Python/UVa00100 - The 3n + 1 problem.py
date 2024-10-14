while 1:
	try:
		n,m = map(int,input().split())
	except: 
		break
		
	def run(num):
		if num == 1:
			return 1
		elif num % 2 != 0:
			return 1 + run(3*num+1)
		else:
			return 1 + run(num/2)
	
	out = 0
	for i in range(min(n,m),max(n,m)+1):
		out = max(out,run(i))
		
	print(n,m,out)
