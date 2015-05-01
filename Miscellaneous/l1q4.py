'''
Classification of x-y plane into 2 classes with perceptron algorithm
class 1: points above the line y=x
Class 2: points below the line y=x

'''

import numpy as np
import random

weight=np.array([1,1.0,-1.0])
eta=0.1
N=30 # number of data points
data=np.zeros(shape=(N,3))
label=np.zeros(N,dtype=np.int)

#generate random data points
for i in range(0,N):
	num1=random.uniform(-10,10) # X cordinate
	num2=random.uniform(-10,10)	# Y cordinate
	if num2>num1:
		label[i]=1  # if Y>X positive class
	else:
		label[i]=-1 # else negative class
	data[i]=[1,num1,num2]		

count=0
iteration=0
while True:	
	iteration=iteration+1
	for i in range(0,N):
		pred=np.sign(np.dot(data[i],weight))
		if pred==label[i]:
			count=count+1
			continue
		else:
			weight=weight+eta*(label[i]-pred)*data[i]

	print count
	if count==N:
		break
	else:
		count=0

print weight
print iteration						
