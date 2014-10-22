#!/usr/bin/python
'''

this code aims to  maximize the  function f(x)=sin(pi*x/256)
it uses Genetic Algorithms to find the optimum value
Notations,GA methods & operators used

--population size = 8
--representation of a chromosome = bitstring of length 8 bits
--Reproduction method = Roulete wheel selection
--Cross over = single point cross over with fixed probability 0.5
--Mutation = by flipping a bit in the input string at a random position
--Mutation probability = 0.1
--No of generations = 100

'''

import math
import random
import numpy as np
import string as st

sin=math.sin
pi=math.pi

f=lambda x :sin(pi*x/256)
pop=np.empty(8, dtype='int')
newPop=np.empty(8, dtype='int')
tempPop=np.empty(8, dtype='int')
fval=np.empty(8)
fnorm=np.empty(8)
rand=np.empty(8)
generations=100


####  initializing the population ####
for i in range(0,8):
	pop[i]=random.randrange(0,256)

print 'initial' 
print pop
for k in range(1,generations):

	newPop=1*pop	
	for i in range(0,8):
		fval[i]=f(pop[i])	

	fvalsum=sum(fval)	
	fnorm=fval/fvalsum
	fnorm=np.cumsum(fnorm)

	#print fval
	#print fnorm
####  finding the new population via reproduction ####
####  roulete wheel selection is implemented here  ####
	for i in range(0,8):
		rand[i]=random.uniform(0,1)
		if 0 <= rand[i] < fnorm[0]:
			#print('0 %f %f\n' %(rand[i],fnorm[0]))
			newPop[i]=pop[0]
		elif(fnorm[0] <=rand[i]< fnorm[1]):
			#print('%f %f %f\n' %(fnorm[0],rand[i],fnorm[1]))			
			newPop[i]=pop[1]
		elif(fnorm[1] <=rand[i]< fnorm[2]):
			#print('%f %f %f\n' %(fnorm[1],rand[i],fnorm[2]))			
			newPop[i]=pop[2]
		elif(fnorm[2] <=rand[i]< fnorm[3]):
			#print('%f %f %f\n' %(fnorm[2],rand[i],fnorm[3]))			
			newPop[i]=pop[3]
		elif(fnorm[3] <=rand[i]< fnorm[4]):
			#print('%f %f %f\n' %(fnorm[3],rand[i],fnorm[4]))			
			newPop[i]=pop[4]
		elif(fnorm[4] <=rand[i]< fnorm[5]):
			#print('%f %f %f\n' %(fnorm[4],rand[i],fnorm[5]))			
			newPop[i]=pop[5]
		elif(fnorm[5] <=rand[i]< fnorm[6]):
			#print('%f %f %f\n' %(fnorm[5],rand[i],fnorm[6]))			
			newPop[i]=pop[6]
		elif(fnorm[6] <=rand[i]< fnorm[7]):
			#print('%f %f %f\n' %(fnorm[6],rand[i],fnorm[7]))			
			newPop[i]=pop[7]


	#print pop				
	#print newPop
	newPop=np.array(map(str,newPop))  ##converting numpy array to string
	newPop=newPop.astype('S8')  ## make the string length 8


#####  performing crosss over  #####
#####  single point cross over  #####
	for i in range(0,8,2):
 		randno=random.uniform(0,1)
 		#print randno
 		if(randno>=0.5):
 			point=random.randrange(1,7)
 			#print('%d\n' %(point))
 			tempstr1=np.int_(newPop[i])
 			tempstr2=np.int_(newPop[i+1])
 			num1=format(tempstr1, '008b')
 			num2=format(tempstr2, '008b')
 			#print num1
 			#print num2
 			temp1=num1[point:len(num1)]
 			temp2=num2[point:len(num2)]
 			cross1=num1[0:point]
 			cross2=num2[0:point]
 			#print temp1
 			#print temp2
 			#print cross1
 			#print cross2
 			newPop[i]=cross1+temp2
 			newPop[i+1]=cross2+temp1
 			#print newPop[i]
 			#print newPop[i+1]
 		else:
 			tempstr1=np.int_(newPop[i])
 			tempstr2=np.int_(newPop[i+1])
 			num1=format(tempstr1, '008b')
 			num2=format(tempstr2, '008b')
 			newPop[i]=num1
 			newPop[i+1]=num2
 			#print newPop[i]
 			#print newPop[i+1] 				

####  performing mutation  #####
####  mutation probability = 0.1 is taken  #####
	if(k%10==0):
		for i in range(0,8):
			point=random.randrange(1,7)
			temp=list(newPop[i])
			if(temp[point]=='1'):
				temp[point]='0'
				newPop[i]=''.join(temp)
			else:
				temp[point]='1'
				newPop[i]=''.join(temp)


#### converting newPop back to integers  #####
#### save the individiuals with higher fitness value in population  ####
	for i in range(0,8):
		tempPop[i]=np.int_(newPop[i],2)

	print tempPop	

	#print type(newPop[i])
	for i in range(0,8):
		#print type(newPop[i])					
		#newPop[i]=np.int_(newPop[i],2)
		#print type(tempPop[i])
		#print type(pop[i])				
		tempfval1=f(pop[i])
		tempfval2=f(tempPop[i])
		if(tempfval2 > tempfval1):
			pop[i]=tempPop[i]


for i in range(0,8):
	fval[i]=f(pop[i])	

maxfval=np.amax(fval)
maxidx=fval.argmax()
optsol=pop[maxidx]
print('maximum value of the function:%f\n' %(maxfval))
print('optimum solution:%d\n' %(optsol))