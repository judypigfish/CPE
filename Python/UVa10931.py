while(1):
	n = int(input())
	if n == 0: break
	
	out = ""
	a = 0
	while(n>1):
		out += str(n%2)
		if n%2 == 1 :a +=1 
		n = int(n/2)
	if n == 1: 
		out += str(n)
		a+=1
	print(f"The parity of {out[::-1]} is {a} (mod 2).")
