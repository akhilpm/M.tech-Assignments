import numpy as np
import matplotlib.pyplot as plt
#import random

lambdaa=3
mu=5
T=20
no_of_customers=0
timestamp=0
																				
class Customer:
	def __init__(self,arrival_time,service_start_time,service_time):
		self.arrival_time=arrival_time
		self.service_start_time=service_start_time
		self.service_time=service_time
		self.waiting_time=service_start_time-arrival_time
		self.service_end_time=service_start_time+service_time


Customers=[]
while timestamp<T:

	#calculate the parameters for the new customer
	#arrival is poisson with rate lambdaa
	if no_of_customers==0:
		arrival_time=np.random.exponential(lambdaa)
		service_start_time=arrival_time
	else:
		arrival_time=arrival_time+np.random.exponential(lambdaa)
		if arrival_time>T:
			break
		service_start_time=max(arrival_time,Customers[-1].service_end_time)	

	#service time is exponential with rate 1/mu	
	service_time=np.random.exponential(mu)	
	#Add the new customer to the list
	Customers.append(Customer(arrival_time,service_start_time,service_time))	
	no_of_customers=no_of_customers+1
	#increment the clock
	timestamp=arrival_time
	print ('%f :%f\n' %(arrival_time,service_start_time))

waiting_times=[c.waiting_time for c in Customers]
mean_waiting_time=sum(waiting_times)/len(waiting_times)

service_times=[c.service_time for c in Customers]
mean_service_time=sum(service_times)/len(service_times)
utilization=sum(service_times)/timestamp

mean_time=mean_service_time+mean_waiting_time

print 'SUMMARY'
print 'No of Customers:',len(Customers)
print 'mean waiting time:',mean_waiting_time
print 'mean service time:',mean_service_time
print 'mean time in the system:',mean_time
print 'service utilization:',utilization
#print waiting_times

fig=plt.figure()
indx=np.arange(no_of_customers)+1
plt.bar(indx,waiting_times)
#plt.show()
plt.savefig('status.png')

fpw=open('status.dat','w')
fpw.write('Customer No, arrival_time, waiting_time, service_time \n')
count=1
for c in Customers:
	fpw.write('%d,	%f,	%f,	%f\n' %(count,c.arrival_time,c.waiting_time,c.service_time))
	count=count+1
fpw.close()
