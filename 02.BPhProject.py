from basic_setup import *


##################


def distance(p1,p2):
	"""Evaluates Sqrt[(x0-x1)2 +(y0-y1)2 + (z0-z1)2]"""
	return math.sqrt((p1.coord[0]-p2.coord[0]) ** 2 + (p1.coord[1]-p2.coord[1]) ** 2 + (p1.coord[2]-p2.coord[2]) ** 2)
    
def elec_interaction(p1,p2, er):
	"""Electrostatic interaction"""
	r = distance(p1,p2)
	if er == 1 or er == 80:
		d = r * er
	elif er == "MS":
		d = r * (86.9525/(1-7.7839*math.exp((-0.3153)*r))-8.5525)
	return 332.16 * p1.xtra['charge'] * p2.xtra['charge'] / d
	
def vdw_interaction(p1, p2):
	"""vdwenergy between two particles"""
	EPS = math.sqrt(p1.xtra['vdw'].eps * p2.xtra['vdw'].eps)
	SIG = math.sqrt(p1.xtra['vdw'].sig * p2.xtra['vdw'].sig)
	f = SIG / distance(p1,p2)
	return 4. * EPS * (pow(f, 12)-pow(f, 6))
	
def solvation(p):
	return(p.xtra['vdw'].fsrf * float(p.xtra.get('EXP_NACCESS', 0.)))
	
def fold_energy(st):
	eint = 0.
	evdw = 0.
	dG = 0.
	for model in st:
		for chain in model:
			for res1 in chain:
				for res2 in chain:
					if res1 == res2:
						continue
					for p1 in res1:
						dG += solvation(p1)
						for p2 in res2:
							eint = eint + 0.5 * elec_interaction(p1, p2, 'MS')
							if distance(p1,p2) >= 2.0:
								evdw = evdw + 0.5 * vdw_interaction(p1, p2)
	return (eint+evdw+dG)



print(fold_energy(st))
