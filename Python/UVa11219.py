a = int(input())

for i in range(a):
	input()
	now = list(map(int,input().split("/")))
	born = list(map(int,input().split("/")))
	
	if (born[2]>now[2]) or (born[2]==now[2] and born[1]>now[1]) or (born[2]==now[2] and born[1]==now[1] and born[0]>now[0]):
		print(f"Case #{i+1}: Invalid birth date")
	else:
		age = now[2]-born[2]
		if (born[1]>now[1]) or (born[1]==now[1] and born[0]>now[0]):
			age -=1
		
		if age > 130:
			print(f"Case #{i+1}: Check birth date")
		else:
			print(f"Case #{i+1}: {age}")
