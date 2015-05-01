# simulation to generate binomial variates
# method used: Acceptance Rejection Method
# speciality of the algorithm : u(0,1) is generated only once in the process

import time
import random

# Assign the parameters of the distribution here 
p=0.2
n=10

alpha=1/p
beta=1/(1-p)

try:
	while True:
		u=random.random()
		X=0
		for k in range(0,n-1):	
			if u<=p:
				X=X+1
				u=alpha*u
			else:
				u=beta*(u-p)

		print X		
		time.sleep(1)			

except KeyboardInterrupt:
	exit	