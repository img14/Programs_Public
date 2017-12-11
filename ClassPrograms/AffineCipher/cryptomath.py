def gcd(a, b):
	mi = min(a,b)
	ma = max(a,b)
	if mi == 0:
		return ma
	elif mi == 1:
		return mi
	else:
		return gcd(ma%mi,mi)

def lcm(a, b):
	for i in range(max(a,b),a*b+1):
		if i%a == 0 and i%b == 0:
			return i

def mod_inverse(a,m):
	for i in range(0,m):
		if (i*a)%m == 1:
			return i
	return -1

#accounts for gcd != 1
def lin_solve(a,b,c,m):
	d = (c-b)%m
	a = a%m
	g1 = gcd(a,d)
	g2 = gcd(d,m)
	g3 = gcd(a,m)
	if g3 == 1: 
		return(mod_inverse(a,m)*(c-b))%m
	elif g1 == g2 and g2 == g3:
		d = d/g1
		a = a/g1
		m = m/g1
		return(mod_inverse(a,m)*(c-b))%m
	else:
		print("Choose another pair, cannot solve equation")
		return -1

def lin_sys_solve(a,b,c,d,e,f,m):
	x = (mod_inverse((d - e*mod_inverse(b,m)*a), m)*(f - e*mod_inverse(b,m)*c))%m
	y = mod_inverse(b,m)*(c - a*x)%m
	return (x,y)


def lin_inverse(a,b,m):
	return (mod_inverse(a,m)%m, -1*(mod_inverse(a,m)*b)%m)

#For affine specifically, 'b' term is always 1
def a_lin_sys_solve(x1,y1,x2,y2,m):
	x = x2-x1
	y = y2-y1
	return lin_solve(x,0,y,m)

'''
def lin_solve(a,b,c,m):
	return (mod_inverse(a,m)*(c-b))%m
'''

#print(gcd(5,8))
#print(gcd(2,10))
#print(gcd(32,64))
#print(gcd(23,67))