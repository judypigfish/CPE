import math

while 1:
	try:
		a = float(input())
	except:
		break
	
	r4 = a*a*math.pi/4
	z = a*a - r4
	z -= r4 - (a*a*math.pi/6)*2 + a*a*(3**0.5)/4
	y = a*a - r4 - 2*z
	x = a*a - 4*z - 4*y
	print(f"{x:.3f} {y*4:.3f} {z*4:.3f}")
