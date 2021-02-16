import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#compute a single euler step
def euler_step(f,x0,t0,stepWidth):
    x1 = x0 + stepWidth*f(x0,t0)
    return x1

#solves from x1,t1 to x2,t2 in steps no bigger than deltatmax
#deltamax should be powers of 2 to reduce rounding error?
#f is dxdt gradient function
def solve_to(f,x1,t1,h,deltat_max):
    t2 = t1 + h
    if deltat_max < h:
        deltatmaxSteps = int(h/deltat_max) #gives number of delta t_max steps
        r_step = h - deltat_max # remainder step width - just 1 step
        X = [x1] #create lists of x and t values initialized at x1 and t1
        T = [t1] 
        #populate lists
        for i in range(deltatmaxSteps):
            X[i+1] = euler_step(f,X[i],T[i],deltat_max)
        #add final r_step to end of list
        X.append(euler_step(f,X[deltatmaxSteps],T[deltatmaxSteps],r_step))
        x2 = X[-1]
        

    return x2,t2


def solve_ode(euler_step,solve_to):
    X = None
    return X

def our_ode(x,t):
    dxdt = x
    return dxdt

#initial condition
x0 = 1
t = np.linspace(0,10)
x = odeint(our_ode,x0,t)

plt.plot(t,x)

plt.show()
