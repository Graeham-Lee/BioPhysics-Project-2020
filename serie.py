
from BPhProject import *
import matplotlib.pyplot as plt

F=fold_energy(st)


posi=[]
ddG=[]
for model in st:
	for chain in model:
		for res in chain:
			if res.resname != 'GLY' and res.resname != 'ALA':
				f=os.popen('python3 unfold.py '+os.path.dirname(os.path.abspath(__file__)) + '/data/AA_PDB/'+res.resname+'.pdb '+os.path.dirname(os.path.abspath(__file__)) + '/data/AA_PDB/'+res.resname+'.pdbqt')
				dU = 2.174477 - float(f.read())
				posi.append(res._id[1])
				os.system('check_structure -i 1ubq_fixed.pdb -o 1ubq_'+str(res._id[1])+'A.pdb mutateside --mut '+res.resname + str(res._id[1])+'Ala')
				os.system('check_structure -i 1ubq_'+str(res._id[1])+'A.pdb -o 1ubq_'+str(res._id[1])+'A_H.pdb add_hydrogen --add_mode auto')
				os.system('check_structure -i 1ubq_'+str(res._id[1])+'A.pdb -o 1ubq_'+str(res._id[1])+'A_H.pdbqt add_hydrogen --add_mode auto --add_charges')
				f=os.popen('python3 BPhProject.py 1ubq_'+str(res._id[1])+'A_H.pdb 1ubq_'+str(res._id[1])+'A_H.pdbqt')
				mF=float(f.read())
				dF = mF-F
				ddG.append(dF-dU)
				print(posi)
				print(ddG)
				
lines = plt.plot(posi, ddG, posi, dG, 'o')  

plt.setp(lines[0], linewidth=1)  
plt.setp(lines[1], linewidth=2)  
 
plt.show()
				

