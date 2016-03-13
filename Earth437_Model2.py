#Start of the code

#Importing Math Function:
import math
#Importing Plotting function

import matplotlib.pyplot as plt

#Introduction
print "\n\nGreetings, "
print "- The Purpose of this program is to compare the two simple analytical models from single-plan," 
print "2-D hydraulic farcturing."
print "- The names of these models are called 'Perkins-Kern-Nordgen (PKN) Model' and 'Geertsma-de Klerc Model.(GdK)'"
print "- By raw inputing the parameters into this program, the user will be able determine" 
print "the differences in the predictions for the two models, including the effects of material parameters."

#Printing Name and ID
name = ['Sunghyun Park', 'Yen Hai Huynh', 'Shrutika Sainani','Casey Vanderwerff', 'Daniel Kim']
id = ['20424651', '20429812', '20408067', '20484879', '20428198']
print ""
print "Group Members:"

num0 = 0
hi = 3 #fracture height is assumed to be 3 ft for imperial unit
hm = 0.9144 #3ft in m

for i in name:
	print i + " - "+id[num0]
	num0=num0+1

print "Ver. 1.0"

while True:
	unit = raw_input("\nType 'I' for imperial units or 'M' for metric units (type 'Exit' to exit): ")
	if unit == 'Exit':
		print "Good Bye - Program terminating..."
		break
	elif unit == 'I':
		h = hi
		print "You've selected imperial units"
	elif unit == 'M':
		h = hm
		print "You've selected metric units"
		
	prompt = "\nWhich of the following parameters would you like it to vary? \nType:\n'f' for fluid effect\n's' for stress effect\n'p' for pumping rate\n'm' for shear modulus\n(type 'Exit' to exit)\n->  "
	factor = raw_input(prompt)
	if  factor == "Exit":
		print "Good Bye - Program terminating..."
		break
	else:
		print "You've selected %s." % factor
	
	#variance in viscosity			
	if unit == 'I' and factor == 'f': 

		mmin = raw_input("Fluid viscosity (cp) - Lower limit: ")
		minc = raw_input("Fluid viscosity (cp) - Increment: ")
		mmax = raw_input("Fluid viscosity (cp) - Upper limit: ")
		
		try:
			mmin = float(mmin)
			minc = float(minc)
			mmax = float(mmax)
			
			if mmin > mmax or minc > mmax:
				print "There is a problem with the inputs. Please try again."
				continue
			
			m = []
			n = 0
			
			while mmin + n*minc<=mmax:
				m.append(mmin+n*minc)
				n = n + 1
			
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue

		q = raw_input("Pumping Rate (bbl/min): ")
		try:
			q = float(q)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
			
		g = raw_input("Shear modulus of material (psi): ")
		try:
			g = float(g)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
			
		v = raw_input("Drained Possion's ratio: ")
		try:
			v = float(v)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
				
		smin = raw_input("in-situ stress (S minimum, psi): ")
		try:
			smin = float(smin)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
				
		t = raw_input("Passed Time (min): ")	
		try:
			t = float(t)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue		
		break
		
		#Variance in-situ stress
	elif unit == 'I' and factor == 's':

		sminmin = raw_input("in-situ stress (S minimum, psi) - Lower limit: ")
		smininc = raw_input("in-situ stress (S minimum, psi) - Increment: ")
		sminmax = raw_input("in-situ stress (S minimum, psi) - Upper limit: ")
		try:
			sminmin = float(sminmin)
			smininc = float(smininc)
			sminmax = float(sminmax)
			
			if sminmin > sminmax or smininc > sminmax:
				print "There is a problem with the inputs. Please try again."
				continue
				
			smin = []
			n = 0
			
			while sminmin + n*smininc <= sminmax:
				smin.append(sminmin+n*smininc)
				n = n+1
				
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
		
		q = raw_input("Pumping Rate (bbl/min): ")
		try:
			q = float(q)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
			
		g = raw_input("Shear modulus of material (psi): ")
		try:
			g = float(g)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
			
		v = raw_input("Drained Possion's ratio: ")
		try:
			v = float(v)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
				
		m = raw_input("Fluid Vsicosity (cp): ")
		try:
			m = float(m)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
				
		t = raw_input("Passed Time (min): ")	
		try:
			t = float(t)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
				
		break
		
		
		#Variance Pumping Rate
	elif unit == 'I' and factor == 'p':

		qmin = raw_input("pumping rate (bbl/min) - Lower limit: ")
		qinc = raw_input("pumping rate (bbl/min) - Increment: ")
		qmax = raw_input("pumping rate (bbl/min) - Upper limit: ")
		try:
			qmin = float(sminmin)
			qinc = float(smininc)
			qmax = float(sminmax)
			
			if qmin > qmax or qinc > qmax:
				print "There is a problem with the inputs. Please try again."
				continue
				
			q = []
			n = 0
			
			while qmin + n*qinc <= qmax:
				q.append(qmin+n*qinc)
				n = n+1
				
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue

	
		smin = raw_input("in-situ stress (S minimum, psi): ")
		try:
			smin = float(smin)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
			
		g = raw_input("Shear modulus of material (psi): ")
		try:
			g = float(g)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
			
		v = raw_input("Drained Possion's ratio: ")
		try:
			v = float(v)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
				
		m = raw_input("Fluid Vsicosity (cp): ")
		try:
			m = float(m)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
				
		t = raw_input("Passed Time (min): ")	
		try:
			t = float(t)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
				
		
		
		#Variance shear modulus
	elif unit == 'I' and factor == 'm':

		gmin = raw_input("shear modulus (psi) - Lower limit: ")
		ginc = raw_input("shear modulus (psi) - Increment: ")
		gmax = raw_input("shear modulus (psi) - Upper limit: ")
		try:
			gmin = float(gmin)
			ginc = float(ginc)
			gmax = float(gmax)
			
			if gmin > gmax or ginc > gmax:
				print "There is a problem with the inputs. Please try again."
				continue
				
			g = []
			n = 0
			
			while gmin + n*ginc <= gmax:
				g.append(gmin+n*ginc)
				n = n+1
				
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue

		q = raw_input("Pumping Rate (bbl/min): ")
		try:
			q = float(q)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
			
		smin = raw_input("in-situ stress (S minimum, psi): ")
		try:
			smin = float(smin)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
			
		v = raw_input("Drained Possion's ratio: ")
		try:
			v = float(v)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
				
		m = raw_input("Fluid Vsicosity (cp): ")
		try:
			m = float(m)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
				
		t = raw_input("Passed Time (min): ")	
		try:
			t = float(t)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue

		break