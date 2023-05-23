while(1):
	a,b,c,d,L = map(int,input().split())
	if(a == 0 and b == 0 and c == 0 and d == 0 and L == 0):
		break
	s = [1 for i in range(L+1) if (a*i*i + b*i + c) % d == 0]
	print(len(s))
