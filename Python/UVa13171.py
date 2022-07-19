n = int(input())

for i in range(n):
	M,Y,C,now = input().split()
	M,C,Y = int(M),int(C),int(Y)
	for j in range(len(now)):
		if now[j] == "M": 
			M -= 1
		elif now[j] == "C":
			C-=1
		elif now[j] == "Y":
			Y-=1
		elif now[j] == "R":
			M-=1
			Y-=1
		elif now[j] == "G":
			Y-=1
			C-=1
		elif now[j] == "V":
			C-=1
			M-=1
		elif now[j] == "B":
			M-=1
			C-=1
			Y-=1
	
	if M < 0 or Y < 0 or C < 0:
		print("NO")
	else:
		print("YES",M,Y,C)
