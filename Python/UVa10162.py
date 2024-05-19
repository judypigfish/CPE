t = [0]
for i in range(1,20):
	t.append(str(int(t[i-1])+i**i)[-1])

while 1:
	s = int(input())
	if s == 0:
		break
	
	v = int(str(s)[-1:-3:-1][::-1])
	out = int(int(t[v%20]) + v//20*4) % 10
	print(out)
