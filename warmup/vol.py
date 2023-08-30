#!/usr/bin/env python3
import os
from math import pi
import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt
from itertools import cycle

lines = ['-','--','-.',':','.',',','o','v','^','<','>','1','2','3','4','s','p','*','h','H','+','x','D','d','|','_']
linecycler = cycle(lines)

# myDim = []
# myRad = []
count = 0

arrRads=[]

for j in range(31,41):
	outX=[]
	outY=[]
	curRad=j/20	
	arrRads.append(curRad)
	for i in range(2,50) :
		outY.append((np.pi**(i/2.0)) * curRad**i / (gamma((i/2.0)+1))) #(arrVol[i][j])
		outX.append(i)
	f_1=plt.figure(1,figsize=(10,9))
	plt.plot(outX,outY,next(linecycler))
	plt.xlabel('Dimension')
	plt.ylabel('Volume')
	plt.title('Hypersphere volume by Dimension, for varying radii')
	plt.legend(arrRads,bbox_to_anchor=(1.1, 0.5), loc='center right',labelspacing = 0.25, title='Radius')

'''
	f=plt.figure(2)
	plt.yscale("log")
	plt.plot(outX,outY)
'''

for i in range(0, len(outY)):
	print(i, outY[i])

outX=[]
outY=[]

# for j in range(0,len(myRad)):
	# #print(j)
	# #for i in range(0, len(arrVol[j])) :
	# for i in range(2,len(myDim)) :
		# if(arrVol[i][j])<(1*10**(1) and arrVol[i][j] > (1*10**(-2 ))):
			# #print(myDim[i])#, myRad[j])
			# #print(arrVol[i][j])
			# outX.append(myDim[i])
			# outY.append(arrVol[i][j])

	#g=plt.figure(3)
	#plt.yscale("log")
	#plt.plot(outX,outY)

plt.show()




		
