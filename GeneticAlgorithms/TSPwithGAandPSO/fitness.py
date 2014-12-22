'''

*****************************************
function that calculates the cost of a tour
Author:Akhil P M
Input:individual=a tour in TSP,cost=an N*N matrix
Output:length of the tour
*****************************************

'''



def calculate_fitness(individual,cost):	
	fit_val=0
	length=len(individual)

	for i in range(0,len(individual)-1):
		#print individual[i]-1,individual[i+1]-1
		fit_val+=cost[individual[i]-1,individual[i+1]-1]
		#print cost[individual[i]-1,individual[i+1]-1]
	
	fit_val+=cost[individual[0]-1,individual[length-1]-1]
	#print cost[individual[0]-1,individual[length-1]-1]
	#print fit_val
	return fit_val
