t = int(input())

for i in range(t):
	n = int(input())
	a = []
	for j in range(n):
		a.append([0]*n)
		s = input()
		for k in range(len(s)):
			a[j][k] = s[k]
			
	m = int(input())
	for j in range(m):
		now = input().split()
		if now[0] == "transpose":
			new = []
			for x in range(n):
				g = []
				for y in range(n):
					g.append(a[y][x])
				new.append(g)
			a = new
			
		elif now[0] == "row":
			aa,bb = int(now[1])-1,int(now[2])-1
			s = a[aa]
			a[aa] = a[bb]
			a[bb] = s
			
		elif now[0] == "col":
			aa,bb = int(now[1])-1,int(now[2])-1
			g = []
			for x in range(n):
				g.append(a[x][aa])
			
			for x in range(n):
				a[x][aa] = a[x][bb]
				a[x][bb] = g[x]
		
		elif now[0] == "inc":
			for x in range(n):
				for y in range(n):
					a[x][y] = int(a[x][y])+1
		
		elif now[0] == "dec":
			for x in range(n):
				for y in range(n):
					a[x][y] = int(a[x][y])-1
	print(f"Case #{i+1}")
	for j in range(n):
		out = ""
		for k in range(n):
			if int(a[j][k]) < 0:
				a[j][k] = int(a[j][k])+10
			if int(a[j][k]) > 9:
				a[j][k] = int(a[j][k])-10
			out += str(a[j][k])
		print(out)
	print()
