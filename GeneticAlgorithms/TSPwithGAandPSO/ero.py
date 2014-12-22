'''

**************************************************
edge recombination crossover operator
Author:Akhil P M
interface:crossOver(parent1,parent2)
Input:two parent chromosomes of a TSP tour
Output:the offspring produced after crossover
**************************************************

NOTE:in the parent chromosome cities should be numbered from 1 to n

'''

import random
import numpy as np



#this will return a numpy array with adjacency list as sets in the array
def create_adjacency_list(p1,p2):
	adj_list=np.empty(0, dtype='int')

	for i in range(0,len(p1)):
		#assuming cities are numbered from 1 to n
		element=i+1

		#processing the first parent
		idx=np.where(p1==element)
		#print idx
		position=idx[0][0]
		if (position!=0 and position!=len(p1)-1):
			left1=p1[position-1]
			right1=p1[position+1]
		elif position==0:
			left1=p1[len(p1)-1]
			right1=p1[1]
		else:
			left1=p1[len(p1)-2]
			right1=p1[0]	

		#processing the second parent
		idx=np.where(p2==element)
		position=idx[0][0]
		if (position!=0 and position!=len(p2)-1):
			left2=p2[position-1]
			right2=p2[position+1]
		elif position==0:
			left2=p2[len(p2)-1]
			right2=p2[1]
		else:
			left2=p2[len(p2)-2]
			right2=p2[0]			
			
		adj_list=np.append(adj_list,[{left1,right1,left2,right2}])

	#print adj_list	
	return adj_list	


#deletes selected node from the adjacency list
def remove_selected_node(node,adj_list):
	for i in range(0,len(adj_list)):
		if node in adj_list[i]:
 	 	  adj_list[i].remove(node)

 	#print adj_list

def random_unvisited_node(child,p1):
	for i in range(0,len(p1)):
		if p1[i] not in child:
			return p1[i]

#perform the edge recombination cross over operation
def cross_over(parent1,parent2):
	child=np.empty(0, dtype='int')
	adj_list=create_adjacency_list(parent1,parent2)
	
	#randomly select the starting node of the offspring
	starter=random.randrange(0,2)
	if starter==0:
		child=np.append(child,parent1[0])
	else:
		child=np.append(child,parent2[0])


	for i in range(0,len(parent1)):
		current=child[i]
		current_adj=[]

		#remove the current node from the adjacency list
		remove_selected_node(current,adj_list) 
		current_adj=list(adj_list[current-1])
		#print current_adj
		#print '----------------------------------'


		#if the adjacency list of current is non-empty,select one with min no of nodes
		#in its adjacent list
		if len(current_adj)!=0:
			len_min_adj=5
			for j in range(0,len(current_adj)):
				temp=list(adj_list[current_adj[j]-1])
				#print temp
				if len(temp)<len_min_adj:
					next=current_adj[j]
					len_min_adj=len(temp)

		#else randomly choose a node that is not added to the child
		else:
			next=random_unvisited_node(child,parent1)

		#print next	
		#append the selected node to the child
		child=np.append(child,next)

	
	child=np.delete(child,len(child)-1)	
	return child