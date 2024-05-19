s = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
d = {}
for i in range(1,len(s)):
	d[s[i]] = s[i-1]

while 1:
	try:
		st = input()
	except:
		break
	
	out = ""
	for i in st:
		if i in d.keys():
			out += d[i]
		else:
			out += i
	print(out)
