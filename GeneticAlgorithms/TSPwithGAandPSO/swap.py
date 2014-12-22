'''

**************************************************
SWAP operator for PSO
Author:Akhil P M
Input(get_swap_sequence): target position & current position
Output(get_swap_sequence):the swap sequence to reach the target
Input(apply_swap_sequence):current position & swap sequence
Output(apply_swap_sequence):resultant position

**************************************************

'''

import numpy as np
import random

def get_swap_sequence(target,current):

	sequence=np.zeros((0,2))
	for i in range(0,len(target)):

		if target[i]!=current[i]:
			temp=np.where(current==target[i])
			pos=temp[0][0]
			temp_pos=current[i]
			current[i]=current[pos]
			current[pos]=temp_pos
			sequence=np.concatenate((sequence,[[i,pos]]))

	return sequence

def apply_swap_sequence(tour,sequence):

	for i in range(0,len(sequence)):
		idx1=sequence[i][0]
		idx2=sequence[i][1]
		temp=tour[idx1]
		tour[idx1]=tour[idx2]
		tour[idx2]=temp
		
	return tour

def get_random_sequence(n):
		sequence=np.zeros((0,2))
		for i in range(0,8):
			no1=random.randrange(1,n)
			no2=random.randrange(1,n)
			sequence=np.concatenate((sequence,[[no1,no2]]))

		return sequence				