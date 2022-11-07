while(1):
	try:
		a = input()
		b = input()
	except:
		break
	
	a = [ord(a[i]) for i in range(len(a))]
	b = [ord(b[i]) for i in range(len(b))]
	a.sort()
	b.sort()

	na,nb=[],[]
	s,m=0,0
	for i in range(len(a)):
		if a[i] != s:
			na.append(1)
			s = a[i]
		else:
			na[len(na)-1] += 1
	na.sort()
	
	for i in range(len(b)):	
		if b[i] != m:
			nb.append(1)
			m = b[i]
		else:
			nb[len(nb)-1] += 1
	nb.sort()
	
	if len(na) == len(nb):
		x,y=1,1
		for i in range(len(na)):
			if na[i]<nb[i]:
				x=0
			if na[i]>nb[i]:
				y=0
		if x==1 or y==1:
			print("YES")
		else:
			print("NO")
	else:
		print("NO")
