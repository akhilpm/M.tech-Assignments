#!/usr/bin/python
#import math

'''
implementation of 0/1 knapsack problem with GA 
profit & weight values are supplied from an array stored in the program

Notations,GA methods & operators used

--population size = 8
--representation of a chromosome = a string of length same as no of items
  with values ranging from 0 to no of items
  ith value in a chromosome string represents no of times the ith item is included in the
  knapsack.
--Reproduction method = Roulete wheel selection
--Cross over = single point cross over with fixed probability 0.5
--Mutation = by assigning new no items at a random position
--Mutation probability = 0.1
--No of generations = 100

'''

import random
import numpy as np
import string as st

#sin=math.sin
#pi=math.pi

def f(str1):
	weightsum=0
	profitsum=0
	temp=list(str1)
	for i in range(0,len(str1)):
		wtemp=np.int_(temp[i])
		wtempsum=weightsum+wtemp*weight[i]
		if wtempsum>maxcap:
			profitsum=1
			break
		else:
			weightsum=wtempsum	
			profitsum=profitsum+wtemp*profit[i]

	#print profitsum		
	return profitsum		


pop=np.empty(8, dtype='string')
newPop=np.empty(8, dtype='string')
tempPop=np.empty(8, dtype='string')
fval=np.empty(8)
fnorm=np.empty(8)
rand=np.empty(8)
generations=100

maxcap=15
profit=[10,2,7,5]
weight=[3,1,4,7]

pop=pop.astype('S4')
newPop=newPop.astype('S4')

for i in range(0,8):
	pop[i]='\0'
	newPop[i]='\0'

####  initializing the population ####
for i in range(0,8):
	for j in range(0,4):
		temp=random.randrange(0,5)
		numstr=format(temp)
		pop[i]=pop[i]+numstr

print 'initial' 
print pop
for k in range(1,generations):

	newPop=np.copy(pop)	
	for i in range(0,8):
		#number=np.int_(pop[0],2)
		fval[i]=f(pop[i])	

	fvalsum=sum(fval)	
	fnorm=fval/fvalsum
	fnorm=np.cumsum(fnorm)
	#print fnorm

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
	#newPop=np.array(map(str,newPop))  ##converting numpy array to string
	#newPop=newPop.astype('S8')  ## make the string length 8


#####  performing crosss over  #####
#####  single point cross over  #####
	for i in range(0,8,2):
 		randno=random.uniform(0,1)
 		#print randno
 		if(randno>=0.5):
 			point=random.randrange(1,3)
 			#print('%d\n' %(point))
 			tempstr1=newPop[i]
 			tempstr2=newPop[i+1]
 			#num1=format(tempstr1, '004b')
 			#num2=format(tempstr2, '004b')
 			#print num1
 			#print num2
 			temp1=tempstr1[point:len(tempstr1)]
 			temp2=tempstr2[point:len(tempstr2)]
 			cross1=tempstr1[0:point]
 			cross2=tempstr2[0:point]
 			#print temp1
 			#print temp2
 			#print cross1
 			#print cross2
 			newPop[i]=cross1+temp2
 			newPop[i+1]=cross2+temp1
 			#print newPop[i]
 			#print newPop[i+1]


####  performing mutation  #####
####  mutation probability = 0.1 is taken  #####
	#print type(newPop[3])
	if(k%10==0):
		for i in range(0,8):
			point=random.randrange(1,3)
			temp=list(newPop[i])
			num=random.randrange(0,5)
			num=format(num)
			temp[point]=num
			newPop[i]=''.join(temp)


#### converting newPop back to integers  #####
#### save the individiuals with higher fitness value in population  ####
#	for i in range(0,8):
#		tempPop[i]=np.int_(newPop[i],2)

	print newPop	

	#print type(newPop[i])
	for i in range(0,8):
		#print type(newPop[i])					
		#newPop[i]=np.int_(newPop[i],2)
		#print type(tempPop[i])
		#print type(pop[i])				
		tempfval1=f(pop[i])
		tempfval2=f(newPop[i])
		if(tempfval2 > tempfval1):
			pop[i]=newPop[i]

	#print 'hello'
	#print pop		


for i in range(0,8):
	fval[i]=f(pop[i])	

maxfval=np.amax(fval)
maxidx=fval.argmax()
optsol=pop[maxidx]
print('maximum value of the function:%f\n' %(maxfval))
print('optimum solution:%s\n' %(optsol))