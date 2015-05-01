
'''
Learning strategy: value iteration
Action Directory
================================
1 = North(N)
2 = South(S)
3 = East(E)
4 = West(W)
================================
'''


import numpy as np 
import time

eps=np.exp(-9) 
gama=1
no_of_states=12
vpi=[]
vpi_old=np.zeros(shape=(3,4))
vpi_new=np.zeros(shape=(3,4))
N=1
S=2
E=3
W=4
last_norm=eps

class Cell:

	def __init__(self,y,x,reward,val=0):
		self.x=x
		self.y=y
		self.reward=reward
		self.action=0
		self.vpi_val=val

	def take_action(self,x,y,action,vpiOld):
		cost=0
		if action==N:
			xnew=x
			ynew=y-1	
			if(ynew<1):
				ynew=y
			elif(xnew==2 and ynew==2):
				ynew=y	
			cost=cost+0.8*vpiOld[ynew-1,xnew-1]
			#reward with LEFT transition
			xnew=x-1
			ynew=y
			if(xnew<1):
				xnew=x	
			elif(xnew==2 and ynew==2):
				xnew=x	
			cost=cost+0.1*vpiOld[ynew-1,xnew-1]
			#reward with RIGHT transition
			xnew=x+1
			ynew=y
			if(xnew>4):
				xnew=x	
			elif(xnew==2 and ynew==2):
				xnew=x	
			cost=cost+0.1*vpiOld[ynew-1,xnew-1]
			#print('%d %d N %0.3f \n' %(y,x,cost))

		elif action==S:
			xnew=x
			ynew=y+1	
			if(ynew>3):
				ynew=y
			elif(xnew==2 and ynew==2):
				ynew=y	
			cost=cost+0.8*vpiOld[ynew-1,xnew-1]
			#reward with LEFT transition
			xnew=x-1
			ynew=y
			if(xnew<1):
				xnew=x	
			elif(xnew==2 and ynew==2):
				xnew=x	
			cost=cost+0.1*vpiOld[ynew-1,xnew-1]
			#reward with RIGHT transition
			xnew=x+1
			ynew=y
			if(xnew>4):
				xnew=x	
			elif(xnew==2 and ynew==2):
				xnew=x	
			cost=cost+0.1*vpiOld[ynew-1,xnew-1]									
			#print('%d %d S %0.3f \n' %(y,x,cost))			

		elif action==E:
			xnew=x+1
			ynew=y	
			if(xnew>4):
				xnew=x
			elif(xnew==2 and ynew==2):
				xnew=x	
			cost=cost+0.8*vpiOld[ynew-1,xnew-1]
			#reward with LEFT transition
			xnew=x
			ynew=y+1
			if(ynew>3):
				ynew=y	
			elif(xnew==2 and ynew==2):
				ynew=y	
			cost=cost+0.1*vpiOld[ynew-1,xnew-1]
			#reward with RIGHT transition
			xnew=x
			ynew=y-1
			if(ynew<1):
				ynew=y	
			elif(xnew==2 and ynew==2):
				ynew=y	
			cost=cost+0.1*vpiOld[ynew-1,xnew-1]
			#print('%d %d E %0.3f \n' %(y,x,cost))

		elif action==W:
			xnew=x-1
			ynew=y	
			if(xnew<1):
				xnew=x
			elif(xnew==2 and ynew==2):
				xnew=x	
			cost=cost+0.8*vpiOld[ynew-1,xnew-1]
			#reward with LEFT transition
			xnew=x
			ynew=y+1
			if(ynew>3):
				ynew=y	
			elif(xnew==2 and ynew==2):
				ynew=y	
			cost=cost+0.1*vpiOld[ynew-1,xnew-1]
			#reward with RIGHT transition
			xnew=x
			ynew=y-1
			if(ynew<1):
				ynew=y	
			elif(xnew==2 and ynew==2):
				ynew=y	
			cost=cost+0.1*vpiOld[ynew-1,xnew-1]
			#print('(%d %d) W %0.3f \n' %(y,x,cost))


		return cost	

#initialize the value of vpi, cell position, reward etc
for j in range (0,3):
	for i in range(0,4):
		if (j+1==1 and i+1==4):
			vpi.append(Cell(j+1,i+1,1))
		elif (j+1==2 and i+1==4):	
			vpi.append(Cell(j+1,i+1,-1))
		else:
			vpi.append(Cell(j+1,i+1,0.2))	

#for k in range (0,no_of_states):	
#	print('%d %d %0.3f %d \n'%(vpi[k].y,vpi[k].x,vpi[k].vpi_val,vpi[k].action))

# Repeat value iteration until convergence
count=0
while True:
	vpi_old=np.copy(vpi_new)
	vpi_new=np.zeros(shape=(3,4))

	for k in range (0,no_of_states):
		x=vpi[k].x
		y=vpi[k].y
		temp=np.zeros(4)
		if(y==2 and x==2):  # hidden state
			continue
		#elif(y==1 and x==4):  # goal state (3,4)
		#	vpi[k].vpi_val=1
		#	vpi_new[y-1,x-1]=1
		#	continue
		elif(y==2 and x==4):  # trap state !
			vpi[k].vpi_val=-1
			vpi_new[y-1,x-1]=-1
			continue
		# take action NORTH	
		temp[0]=vpi[k].take_action(x,y,N,vpi_old)
		# take action SOUTH	
		temp[1]=vpi[k].take_action(x,y,S,vpi_old)
		# take action EAST	
		temp[2]=vpi[k].take_action(x,y,E,vpi_old)
		# take action WEST	
		temp[3]=vpi[k].take_action(x,y,W,vpi_old)

		#consider the action with max reward for getting the optimal policy
		idx=temp.argmax()
		vpi[k].action=idx+1
		vpi_new[y-1,x-1]=vpi[k].reward+gama*temp[idx]	
		vpi[k].vpi_val=vpi_new[y-1,x-1]

	#check for convergence
	tempX=vpi_old.reshape(12,1)
	tempY=vpi_new.reshape(12,1)
	print last_norm-np.linalg.norm(tempX-tempY) 
	if abs(last_norm-np.linalg.norm(tempX-tempY))<eps:
		break
	last_norm=np.linalg.norm(tempX-tempY)
	#print vpi_old
	#for k in range (0,no_of_states):	
	#	print('%d %d %0.3f %d \n'%(vpi[k].y,vpi[k].x,vpi[k].vpi_val,vpi[k].action))	
	print np.linalg.norm(tempX-tempY)	
	print '\n'	
	count=count+1
	print count
	#raw_input("...Press Enter to continue...")
	#time.sleep(3)

print vpi_old
for k in range (0,no_of_states):
	if vpi[k].action==1:
		print('%d %d  N \n'%(vpi[k].y,vpi[k].x))
	elif vpi[k].action==2:	
		print('%d %d  S \n'%(vpi[k].y,vpi[k].x))
	elif vpi[k].action==3:	
		print('%d %d  E \n'%(vpi[k].y,vpi[k].x))
	else:	
		print('%d %d  W \n'%(vpi[k].y,vpi[k].x))			

