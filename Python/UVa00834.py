while(1):
	try:
		a,b = map(int,input().split())
		out = ""
		num = 0
		while(1):
			if num == 1:
				out += ";"
			elif num > 1:
				out += ","
			out += str(int(a/b))
			num +=1 
			h = a % b
			a = b
			b = h 
			if(a <= 1 and b <= 1) or b == 0:
				break
		print(f"[{out}]")	
	except:
		break
