# Solving TSP with a Hybrid Algorithm of PSO & GA
# Here we used edge recombination operator proposed for GA to prevent the
# premature convergence of PSO

import numpy as np
import random
import math
import fitness  as fit
import ero
import swap
#import eero as ero

cities=26
no_of_particles=60
iterations=3000
cost=np.loadtxt('fri26_d.txt')
counter=0 #variable used to terminate when convergence occurs 
#min_cost=qselect.get_min(cost)
#count=0

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


	def update_velocity(self,seq1,seq2,iteration):
		sequence=np.zeros((0,2))
		c1=0.1
		#if iteration<150:	
		c2=random.uniform(0,1)
		c3=random.uniform(0,1)
		#else:
		#	c2=random.uniform(0,0.5)
		#	c3=random.uniform(0,0.5)	
	   	#c1=0.95-0.95*iteration/500
		#c2=0.05+0.95*iteration/500
		#c3=0.05+0.95*iteration/500
		#c=np.array([c1,c2,c3])
		#cvalsum=sum(c)
		#cnorm=c/cvalsum
		#cnorm=np.cumsum(cnorm)
		#randno=random.uniform(0,1)
		#if 0 <= randno < cnorm[0]:
		#	c1=math.ceil(c1*len(self.vel))
		#	sequence=np.concatenate((sequence,self.vel[0:int(c1)]))
		#elif cnorm[0] <=randno< cnorm[1]:
		#	c2=math.ceil(c2*len(seq1))
		#	sequence=np.concatenate((sequence,seq1[0:int(c2)]))
		#elif cnorm[1] <=randno< cnorm[2]:
		#	c3=math.ceil(c3*len(seq2))
		#	sequence=np.concatenate((sequence,seq2[0:int(c3)]))
					
		c1=math.ceil(c1*len(self.vel))
		c2=math.ceil(c2*len(seq1))
		c3=math.ceil(c3*len(seq2))
		sequence=np.concatenate((sequence,self.vel[0:int(c1)]))
		#if c2>=1:
		#	sequence=np.concatenate((sequence,seq1))
		#	c2=c2-1
		sequence=np.concatenate((sequence,seq1[0:int(c2)]))
		#if c3>=1:
		#	sequence=np.concatenate((sequence,seq2))
		#	c3=c3-1
		sequence=np.concatenate((sequence,seq2[0:int(c3)]))
		return sequence


base=np.arange(cities)
base=base+1
base=np.random.permutation(base)
gbest_fit=fit.calculate_fitness(base,cost)
pop=[]
flag=0



#Initialize the particle positions,velocities,fitness
for i in range(0,no_of_particles):
	temp1=np.random.permutation(base)
	temp2=np.random.permutation(base)
	fit_val1=fit.calculate_fitness(temp1,cost)
	fit_val2=fit.calculate_fitness(temp2,cost)

	if fit_val1<=fit_val2:
	 	#sequence=swap.get_swap_sequence(temp1,np.copy(temp2))
	 	#sequence=np.random.permutation(sequence)
	 	sequence=swap.get_random_sequence(cities)
	 	if len(sequence)!=0:
			pop.append(Particle(temp1,fit_val1,temp2,fit_val2,sequence))
	 	else:	 
			pop.append(Particle(temp1,fit_val1,temp2,fit_val2,[[1,2]]))

		if fit_val1<gbest_fit:
			flag=1
			Particle.gbest=np.copy(temp1)
			gbest_fit=fit_val1	

	else:
	 	#sequence=swap.get_swap_sequence(temp2,np.copy(temp1))
	 	#sequence=np.random.permutation(sequence)
	 	sequence=swap.get_random_sequence(cities)
		if len(sequence)!=0:
			pop.append(Particle(temp2,fit_val2,temp1,fit_val1,sequence))
	 	else:	 
			pop.append(Particle(temp2,fit_val2,temp1,fit_val1,[[1,2]]))

		if fit_val2<gbest_fit:
			flag=1
			Particle.gbest=np.copy(temp2)
			gbest_fit=fit_val2		

if flag==0:
	Particle.gbest=np.copy(base)

print gbest_fit
#iterations of hybrid algo starts here
gbest_fit=fit.calculate_fitness(Particle.gbest,cost)
temp_fit=gbest_fit
flag=0

for k in range(0,iterations):

	for i in range(0,no_of_particles):
		child=ero.cross_over(pop[i].pos,pop[i].pbest)
		fit_val=fit.calculate_fitness(child,cost)

		#if fitness of child is higher than pbest,update pbest
		if fit_val<pop[i].pbest_fit:
			pop[i].pbest=np.copy(child)
			pop[i].pbest_fit=fit_val

		#if fitness of child is higher than gbest,update gbest
		#if fit_val<gbest_fit:
		#	Particle.gbest=np.copy(child)
		#	gbest_fit=fit_val
		#	flag=0

		child=ero.cross_over(pop[i].pos,Particle.gbest)
		fit_val=fit.calculate_fitness(child,cost)

		if fit_val<gbest_fit:
			Particle.gbest=np.copy(child)
			gbest_fit=fit_val
			flag=0

		#if counter>20:	
		#	child=ero.cross_over(pop[i].pbest,Particle.gbest)
		#	fit_val=fit.calculate_fitness(child,cost)

		#	if fit_val<gbest_fit:
		#		Particle.gbest=np.copy(child)
		#		gbest_fit=fit_val
		#		flag=0

		#if fitness of child is higher than pbest,update pbest
		#if fit_val<pop[i].pbest_fit:
		#	pop[i].pbest=np.copy(child)
		#	pop[i].pbest_fit=fit_val

		#calculate new velocity,update position	
		seq1=swap.get_swap_sequence(pop[i].pbest,np.copy(pop[i].pos))
		seq2=swap.get_swap_sequence(Particle.gbest,np.copy(pop[i].pos))
		new_vel=pop[i].update_velocity(seq1,seq2,k)
		#new_vel=np.random.permutation(new_vel)
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
		
				
		if pop[i].fitness<gbest_fit:
			gbest_fit=pop[i].fitness
			best=i
			flag=1	
	
#	if(k%5==0):
#		count=count+1					

	if flag==1:
		Particle.gbest=np.copy(pop[best].pos)
		gbest_fit=pop[best].fitness
		flag=0				

	print ('%d %d\n' %(k,gbest_fit))

	if temp_fit==gbest_fit:
		counter=counter+1
	else:
		counter=0
		temp_fit=gbest_fit

	#if there is no change in over 20 generations stop the execution
	#ie, convergence has occured
	if counter==200:
		break		


print 'best solution is'
print Particle.gbest
print 'obtained cost of travel'
print gbest_fit
print 'no of iterations'
print k
