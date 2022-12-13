n = int(input())
etc = [2]
now = 2
while(len(etc)<1000):
	now +=1
	f = 1
	for i in etc:
		if now % i == 0:
			f=0
	if f:
		etc.append(now)

for i in range(n):
	s = sorted(input())
	d ={}
	for j in s:
		if j not in d:
			d[j]=1
		else:
			d[j]+=1
	
	out = ""
	for j in d.keys():
		if d[j] in etc:
			out += j
	
	if out == "":
		out = "empty"
	print(f"Case {i+1}: {out}")
