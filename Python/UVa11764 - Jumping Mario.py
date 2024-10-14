T = int(input())
for j in range(T):
	N = int(input())
	s = list(map(int,input().split()))
	
	h,l = 0,0
	for i in range(len(s)-1):
		if s[i] > s[i+1]:
			l += 1
		elif s[i] < s[i+1]:
			h += 1
	print(f"Case {j+1}: {h} {l}")
