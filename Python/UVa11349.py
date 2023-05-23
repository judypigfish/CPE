num = eval(input())
for i in range(num):
	N = int(input().split()[2])
 	s = []
 	for j in range(N):
		s += list(map(int,input().split()))
	
	if s == s[::-1] and min(s) >= 0:
		print(f"Test #{i+1}: Symmetric.")
	else:
		print(f"Test #{i+1}: Non-symmetric.")
