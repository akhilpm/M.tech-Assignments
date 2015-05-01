import math
import numpy as np
 
def rk4(f,x0,y0,x1,h):
    n=(x1-x0)/h
    n=int(n)
    x_val=np.zeros(n+1)
    y_val=np.zeros(n+1)
    x_val[0]=x=x0  #setting initial values
    y_val[0]=y=y0
    for i in range(1,n+1):
        k1=h*f(x, y)
        k2=h*f(x+0.5*h, y+0.5*k1)
        k3=h*f(x+0.5*h, y+0.5*k2)
        k4=h*f(x+h, y+k3)
        x_val[i]=x=x0+i*h
        y_val[i]=y=y+(k1+2*k2+2*k3+k4)/6
    return x_val,y_val

#give the code for computing f' at here 
def f(x, y):
    #return x*sqrt(y)
    return (x-y)/2

#start the process from here 
vx, vy=rk4(f,0,1,3,0.5)
for x, y in list(zip(vx, vy)):
    print(x,y)
 

#++++++++++++OUTPUT+++++++++++++++++++++
(0.0, 1.0)
(0.5, 0.80403645833333337)
(1.0, 0.79440339406331384)
(1.5, 0.89749678395067656)
(2.0, 1.0883825050787741)
(2.5, 1.3476416482425022)
(3.0, 1.6601506000716753)

