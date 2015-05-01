# Congruent method for generating random numbers

import time

a=8121
c=28411
m=134456
xold=1
print '!!!Hit Ctrl-C to STOP!!!'
try:
	while True:
		xnew=(a*xold+c)%m
		print xnew
		xold=xnew
		time.sleep(1)

except KeyboardInterrupt:
	exit		