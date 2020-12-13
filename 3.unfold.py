from basic_setup import *

dG=0.
for model in st:
	for chain in model:
		for res in chain:
			for p in res:
				dG += p.xtra['vdw'].fsrf * float(p.xtra.get('EXP_NACCESS', 0.))
dG -= 2.174477
print(dG)
