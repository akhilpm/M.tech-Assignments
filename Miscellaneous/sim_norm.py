# simulation to generate normal variates
# method used: Acceptance Rejection Method

import time
import random

mu=10
sigma=4
#count=0

try:
	while True:
		y1=random.expovariate(1)
		y2=random.expovariate(1)

		#count=count+1
		#print count
		if y2 >=pow(y1-1,2)/2:
			u=random.random()
			if u<=0.5:
				z=y1
			else:
				z=-y1
			N=mu+sigma*z
			print N		

		time.sleep(1)	# take rest for 1 second !!

except KeyboardInterrupt:
	exit	