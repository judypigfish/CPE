n = int(input())

for i in range(n):
	p = list(map(int,input().split()))

	def run(x,y):
		now = (y+1)*y/2
		now += (y+2)*x+x*(x-1)/2
		return now
		
	print(f"Case {i+1}: {int(run(p[2],p[3]) - run(p[0],p[1]))}")
