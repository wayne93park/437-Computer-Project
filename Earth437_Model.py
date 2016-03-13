
#Importing Math Function:
import math
#Importing Plotting function

import matplotlib.pyplot as plt

#Introduction
print""
print""
print "Greetings, "
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

num0=0

for i in name:
	print i + " - "+id[num0]
	num0=num0+1

print "Ver. 1.0"

#need to do calculations on fluid volume vs. Net pressure at wellbore, fluid volume vs. fracture length, fluid volume vs. maximum width at wellbore'

#User raw_inputs
print ""
print "Please enter the properties as prompted."
print ""

while True:
	unit = raw_input("Type 'I' for imperial units or 'M' for metric units (type 'Exit' to exit): ")

	if unit == "I":
		print "You have selected imperial units."
		print ""
		q = raw_input("Pumping Rate (bbl/min): ")
		try:
			q = float(q)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
			
		m = raw_input("Fluid viscosity (cp): ")
		try:
			m = float(m)
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
				
		h = raw_input("Fracture height (ft): ")
		try:
			h = float(h)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
			
		break
				
	elif unit == "M":
		print "You have selected metric units."
		print""
			
		q = raw_input("Pumping Rate (m^3/s): ")
		try:
			q = float(q)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
				
		m = raw_input("Fluid viscosity (Pa.s): ")
		try:
			m = float(m)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
				
		g = raw_input("Shear modulus of material (GPa): ")		
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
				
		smin = raw_input("in-situ stress (S minimum, Mpa): ")		
		try:
			smin = float(smin)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
			
		t = raw_input("Passed Time (s): ")	
		try:
			t = float(t)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
				
		h = raw_input("Fracture height (m): ")
		try:
			h = float(h)
		except ValueError:
			print "Please enter numeric Value. Please try again."
			continue
	
			#unit conversions (m->i)
			q = q * 377.39 #m3/s -> bbl/min
			m = m * 1000 #Pa.s to cp
			t = t/60 #s -> min
			g = g*145037.73773 #GPa -> psi
			smin = smin * 145.038 #MPa -> psi
			h = h * 3.28084
			
		break

	elif unit == "Exit":
		print "Thank you."
		break
		
	else:
		print "You did not input neither 'I' or 'M'. Please try again.."	
		continue
	
#creating x-axis (time in min)

time = []
num = 0.001

while num < t:
	time.append(num)
	num = num + 0.001

#KGD Model
l1 = [] #length (ft)
w1 = [] #Width (in)
pw1 = [] #Wellbore Pressure (psi)
for x in time:
	l1.append((0.48*(8*g*q**3/((1-v)*m))**(0.16666666666)*x**(0.66666666666)))
	w1.append((1.32*(8*(1-v)*m*q**3/g)**(0.16666666666)*x**(0.33333333333)))
	
for y in l1:
	pw1.append(smin + 0.96*(2*q*m*g**3/((1-v)**3*y**2))**(0.25))


#PKN Model

l2 = [] #length (ft)
w2 = [] #Width (in)
pw2 = [] #Wellbore Pressure (psi)

for x in time:
	l2.append(0.68*(g*q**3/((1-v)*m*h**4))**(0.2)*x**(0.8))
	w2.append(2.5*((1-v)*m*q**2/(g*h))**(0.2)*x**(0.2))
	pw2.append(2.5*(q**2*m*g**4/((1-v)**4*h**6))**(0.2)*x**(0.2))

#plotting for imperial
if unit == "I":
	plt.figure(1)
	plt.subplot(211)
	plt.plot(time, l1, 'r--', time, l2, 'b--')
	plt.legend('KP')
	plt.title("Length vs. Time Comparison between KGD Model & PKN Model")
	plt.ylabel("length (ft)")
	plt.xlabel("time (min)")
	plt.grid(True)

	plt.subplot(212)
	plt.plot(time, w1, 'r--', time, w2, 'b--')
	plt.legend('KP')
	plt.title("Maximum Width vs. Time Comparison between KGD Model & PKN Model")
	plt.ylabel("Maximum width (inch)")
	plt.xlabel("time (min)")
	plt.grid(True)
	
	plt.show()
	
	plt.figure(2)
	plt.plot(time, pw1, 'r--', time, pw2, 'b--')
	plt.legend('KP')
	plt.title("Wellbore Pressure vs. Time Comparison between KGD Model & PKN Model")
	plt.ylabel("Wellbore Pressure (psi)")
	plt.xlabel("time (min)")
	plt.grid(True)
		
		
	plt.show()
	
#plotting for metric
elif unit == "M":
	#Converting unit again.
	l1m=[]
	w1m=[]
	pw1m=[]
	l2m=[]
	w2m=[]
	pw2m=[]
	
	for j in l1:
		l1m.append(0.3048*j) #ft to m
	for k in l2:
		l2m.append(0.3048*k) #ft to m
	for jj in w1:
		w1m.append(0.0254*jj) #inch to m
	for kk in w2:
		w2m.append(0.0254*kk) #inch to m
	for jjj in pw1:
		pw1m.append(6.89476*jjj) #psi to KPa
	for kkk in pw2:
		pw2m.append(6.9476*kkk) #psi to KPa	
	
	#Plotting
	
	plt.figure(1)
	plt.subplot(211)
	plt.plot(time, l1m, 'r--', time, l2m, 'b--')
	plt.legend('KP')
	plt.title("Length vs. Time Comparison between KGD Model & PKN Model")
	plt.ylabel("length (m)")
	plt.xlabel("time (min)")
	plt.grid(True)
	
	plt.subplot(212)
	plt.plot(time, w1m, 'r--', time, w2m, 'b--')
	plt.legend('KP')
	plt.title("Maximum Width vs. Time Comparison between KGD Model & PKN Model")
	plt.ylabel("Maximum width (m)")
	plt.xlabel("time (min)")
	plt.grid(True)	
	
	plt.show()
	
	plt.figure(2)
	plt.plot(time, pw1m, 'r--', time, pw2m, 'b--')
	plt.legend('KP')
	plt.title("Wellbore Pressure vs. Time Comparison between KGD Model & PKN Model")
	plt.ylabel("Wellbore Pressure (Kpa)")
	plt.xlabel("time (min)")
	plt.grid(True)
	
	plt.show()


	

	
	

