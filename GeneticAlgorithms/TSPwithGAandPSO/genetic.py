'''

**************************************************
GA for solving TSP using edge recombination cross over
Author:Akhil P M
input:cost matrix,no of cities
output:optimum tour obtained from GA
cross over:edge recombination operator
mutation:swap operator
Mutation probability:0.1
**************************************************

'''
import numpy as np
import fitness as fit
import ero
import random

cities=42
pop_size=100
generations=500
base=np.arange(cities)
base=base+1
base=np.random.permutation(base)
pop=np.zeros(shape=(pop_size,cities))
temp_pop=np.zeros(shape=(pop_size,cities))
fval=np.zeros(shape=(pop_size,2))
counter=0 #variable used to terminate when convergence occurs 
#cost=np.loadtxt('gr17_d.txt')
cost=np.loadtxt('dantzig42_d.txt')

#initializing the population
for i in range(0,pop_size):
	 pop[i]=np.random.permutation(base)
	 #print pop[i]


#calculate the fitness of all individuals in the population
for i in range(0,pop_size):
	fval[i][0]=i
	fval[i][1]=fit.calculate_fitness(pop[i],cost)
	#print fval[i][1]

initial_max_fit=min(fval[:, 1])	

#print pop
print initial_max_fit

for k in range(0,generations):
	new_pop=np.zeros(shape=(pop_size,cities))
	#print 'hello'
	#select parents from matting pool with tournament selection
	for i in range(0,pop_size):		
		indx1=random.randrange(0,pop_size)
		indx2=random.randrange(0,pop_size)
		fit_val1=fit.calculate_fitness(pop[indx1],cost)
		fit_val2=fit.calculate_fitness(pop[indx2],cost)
		if fit_val1 <= fit_val2:
			new_pop[i]=pop[indx1]
		else:
			new_pop[i]=pop[indx2]		
	
	#print new_pop		
	#perform cross over b/w randomly selected parents
	for i in range(0,pop_size):
		randno=random.uniform(0,1)
		indx1=random.randrange(0,pop_size)
		indx2=random.randrange(0,pop_size)
		if(randno>=0.5):
			#print new_pop[indx1]
			#print new_pop[indx2]
			new_pop[i]=ero.cross_over(new_pop[indx1],new_pop[indx2])

	#print 'after cross over'	
	#print new_pop	
	#perform mutation
	#mutation probability = 0.1	
	#mutation uses swap operator
	if(k%10==0):
		for i in range(0,pop_size):
			randno=random.uniform(0,1)
			if(randno>=0.5):
				pos1=random.randrange(0,cities)
				pos2=random.randrange(0,cities)
				temp=new_pop[i][pos1]
				new_pop[i][pos1]=new_pop[i][pos2]
				new_pop[i][pos2]=temp

	new_fval=np.zeros(shape=(pop_size,2))			
	for i in range(0,pop_size):
		new_fval[i][0]=i
		new_fval[i][1]=fit.calculate_fitness(new_pop[i],cost)

	#print 'after mutation'	
	#print new_pop	
	
	temp_pop=np.copy(pop)	
	#retain the best individuals to the next generation
	#first sort the new population and old population based on fitness of individuals
	#in decreasing order
	#fval=fval[np.argsort(fval[:, 1])[::-1]]
	#new_fval=new_fval[np.argsort(new_fval[:, 1])[::-1]]

	#now select the best individuals by merging the two populations
	for i in range(0,pop_size):
		idx1=np.argmin(fval[:, 1])
		idx2=np.argmin(new_fval[:, 1])
		if(fval[idx1][1]<=new_fval[idx2][1]):	

			if i==0:
				max_fit=fval[idx1][1]

			pop[i]=temp_pop[idx1]
			temp_pop=np.delete(temp_pop,(idx1),axis=0)
			fval=np.delete(fval,(idx1),axis=0)
		else:

			if i==0:
				max_fit=new_fval[idx2][1]

			pop[i]=new_pop[idx2]
			new_pop=np.delete(new_pop,(idx2),axis=0)
			new_fval=np.delete(new_fval,(idx2),axis=0)

	#if len(fval)>1 or len(new_fval)>1:		
	#	if len(fval)==0:
	#		max_fit=new_fval[0][1]
	#	elif len(new_fval)==0:
	#		max_fit=fval[0][1]
	#	else:
	#		max_fit=min(fval[0][1],new_fval[0][1])						


	#print 'after selection'
	#print pop
	#calculating the fitness of new generation
	fval=np.zeros(shape=(pop_size,2))
	for i in range(0,pop_size):
		fval[i][0]=i
		fval[i][1]=fit.calculate_fitness(pop[i],cost)		

	#checking wether maximum is changing in different iterations	
	if initial_max_fit==max_fit:
		counter=counter+1
	else:
		counter=0
		initial_max_fit=max_fit

	print initial_max_fit	
	#if there is no change in over 20 generations stop the execution
	#ie, convergence has occured
	#if counter==30:
	#	break

#end of generations LOOP

print ('no of generations:%d\n' %(k))
print ('maximul fitness of an individual:%d\n' %(max_fit))
print 'optimum tour'
print pop[0]					