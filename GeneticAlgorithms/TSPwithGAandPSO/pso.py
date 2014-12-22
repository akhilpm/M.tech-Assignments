
'''
**************************************************
PSO for solving TSP with high Mutation Rate
Author: Akhil P M
Particle Size:100
input:cost matrix,no of cities
output:optimum tour obtained from GA
Mutation Probability:0.2
**************************************************
'''



import numpy as np
import random
import math
import fitness  as fit
import ero
import swap


cities=42
no_of_particles=100
iterations=500
#cost=np.loadtxt('data.txt')
cost=np.loadtxt('dantzig42_d.txt')
counter=0 #variable used to terminate when convergence occurs 
flag=0

class Particle:

	gbest=np.arange(cities)

	def __init__(self,pbest,pbest_fit,pos,fit_val,seq):
		self.pos=np.copy(pos)
		self.pbest=np.copy(pbest)
		self.fitness=fit_val
		self.pbest_fit=pbest_fit
		self.vel=np.copy(seq)

	def get_fitness(self,cost):
		return fit.calculate_fitness(self.pos,cost)

	def	update_position(self,seq):
		swap.apply_swap_sequence(np.copy(self.pos),seq)


	def update_velocity(self,seq1,seq2):
		sequence=np.zeros((0,2))
		c1=0.1#random.uniform(0,1)
		c2=random.uniform(0,1)
		c3=random.uniform(0,1)
		c1=math.ceil(c1*len(self.vel))
		c2=math.ceil(c2*len(seq1))
		c3=math.ceil(c3*len(seq2))
		sequence=np.concatenate((sequence,self.vel[0:int(c1)]))
		#sequence=np.concatenate((sequence,seq1))
		sequence=np.concatenate((sequence,seq1[0:int(c2)]))
		#sequence=np.concatenate((sequence,seq2))
		sequence=np.concatenate((sequence,seq2[0:int(c3)]))
		return sequence



base=np.arange(cities)
base=base+1
base=np.random.permutation(base)
#base=np.array([5,2,23,25,22,3,7,8,9,15,11,12,13,14,10,19,16,21,18,17,20,4,26,6,24,1])
gbest_fit=fit.calculate_fitness(base,cost)
pop=[]




#Initialize the particle positions,velocities,fitness
for i in range(0,no_of_particles):
	temp1=np.random.permutation(base)
	temp2=np.random.permutation(base)
	fit_val1=fit.calculate_fitness(temp1,cost)
	fit_val2=fit.calculate_fitness(temp2,cost)
	#print fit_val1,fit_val2

	if fit_val1<=fit_val2:
	 	sequence=swap.get_swap_sequence(temp1,np.copy(temp2))
	 	if len(sequence)!=0:
			pop.append(Particle(temp1,fit_val1,temp2,fit_val2,sequence))
	 	else:	 
			pop.append(Particle(temp1,fit_val1,temp2,fit_val2,[[1,2]]))

		if fit_val1<gbest_fit:
			flag=1
			Particle.gbest=np.copy(temp1)
			gbest_fit=fit_val1	
		#print temp1
		#print temp2

	else:
	 	sequence=swap.get_swap_sequence(temp2,np.copy(temp1))
		if len(sequence)!=0:
			pop.append(Particle(temp2,fit_val2,temp1,fit_val1,sequence))
	 	else:	 
			pop.append(Particle(temp2,fit_val2,temp1,fit_val1,[[1,2]]))

		if fit_val2<gbest_fit:
			flag=1
			Particle.gbest=np.copy(temp2)
			gbest_fit=fit_val2		

		#print temp2
		#print temp1	
if flag==0:
	Particle.gbest=np.copy(base)
print gbest_fit
#iterations of hybrid algo starts here
gbest_fit=fit.calculate_fitness(Particle.gbest,cost)
temp_fit=gbest_fit
flag=0
for k in range(0,iterations):

	for i in range(0,no_of_particles):

		#calculate new velocity,update position	
		seq1=swap.get_swap_sequence(pop[i].pbest,np.copy(pop[i].pos))
		seq2=swap.get_swap_sequence(Particle.gbest,np.copy(pop[i].pos))
		new_vel=pop[i].update_velocity(seq1,seq2)
		#new_pos=pop[i].update_position(new_vel)
		new_pos=swap.apply_swap_sequence(np.copy(pop[i].pos),new_vel)
		#print new_vel
		#print pop[i].pos
		#print new_pos
		#pop[i].pos=swap.apply_swap_sequence(new_pos,pop[i].pos)
		pop[i].vel=swap.get_swap_sequence(new_pos,np.copy(pop[i].pos))				
		pop[i].pos=np.copy(new_pos)
		pop[i].fitness=pop[i].get_fitness(cost)


		if(k%5==0):
			randno=random.uniform(0,1)
			if(randno>=0.5):
				idx1=random.randrange(0,cities)
				idx2=random.randrange(0,cities)
				temp_val=pop[i].pos[idx1]
				pop[i].pos[idx1]=pop[i].pos[idx2]
				pop[i].pos[idx2]=temp_val
				pop[i].fitness=pop[i].get_fitness(cost)

		#if fitness of new position is higher than pbest,update pbest
		if pop[i].fitness<pop[i].pbest_fit:
			pop[i].pbest=np.copy(pop[i].pos)
			pop[i].pbest_fit=pop[i].fitness

		#if fitness of new position is higher than gbest,update gbest
		if pop[i].fitness<gbest_fit:
			gbest_fit=pop[i].fitness
			best=i
			flag=1

	if flag==1:
		Particle.gbest=np.copy(pop[best].pos)
		gbest_fit=pop[best].fitness
		flag=0				
	print gbest_fit		

	if temp_fit==gbest_fit:
		counter=counter+1
	else:
		counter=0
		temp_fit=gbest_fit

	#if there is no change in over 20 generations stop the execution
	#ie, convergence has occured
	#if counter==20:
	#	break		


print 'best solution is'
print Particle.gbest
print 'obtained cost of travel'
print gbest_fit
print 'no of iterations'
print k
