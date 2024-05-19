d = {"E":"3","J":"L","L":"J","S":"2","2":"S","3":"E","Z":"5","5":"Z","H":"H","I":"I","A":"A","M":"M","O":"O","T":"T","U":"U","V":"V","W":"W","X":"X","Y":"Y","1":"1","8":"8"}
while 1:
	try:
		s = input()
	except:
		break
	
	p,m = 1,1
	r = s[::-1]
	if r != s:
		p = 0
		
	c = ""
	for i in range(len(r)):
		if r[i] in d.keys():
			if d[r[i]] != s[i]:
				m=0
				break
		else:
			m = 0
			break

	if p and m:
		print(f"{s} -- is a mirrored palindrome.")
	elif p:
		print(f"{s} -- is a regular palindrome.")
	elif m:
		print(f"{s} -- is a mirrored string.")
	else:
		print(f"{s} -- is not a palindrome.")
	print()
