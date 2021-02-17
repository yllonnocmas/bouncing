import numpy as np

#compute a single euler step
def euler_step(f,x0,t0,stepWidth):
    x1 = x0 + stepWidth*f(x0,t0)
    return x1

#solves from x1,t1 to x2,t2 in steps no bigger than deltatmax
#deltamax should be powers of 2 to reduce rounding error?
#h is width between plotting values of t
def solve_to(dxdt,x1,t1,h,deltat_max):
    if deltat_max < h:
        deltatmaxSteps = int(h/deltat_max) #gives number of delta t_max steps
        r_step = h - (deltatmaxSteps*deltat_max) # remainder step width - just 1 step
        X = np.zeros(deltatmaxSteps + 1) #create arrays of x and t values initialized with x1 and t1
        T = np.zeros(deltatmaxSteps + 1) 
        X[0] = x1
        T[0] = t1
        #populate lists
        for i in range(deltatmaxSteps):
            X[i+1] = euler_step(dxdt,X[i],T[i],deltat_max)
            T[i+1] = T[i] + deltat_max
        #add final r_step to end of array
        np.append(X,euler_step(dxdt,X[-1],T[-1],r_step))
        x2 = X[-1]
    else:
        x2 = euler_step(dxdt,x1,t1,h)    
    return x2

#t is list/array of times to be plotted
def solve_ode(ode,x0,t,deltat_max):
    X = np.zeros(len(t))
    X[0] = x0
    for i in range(len(t)-1):
        h = t[i+1] - t[i] #if t given is not linearly spaced
        X[i+1] = solve_to(ode,X[i],t[i],h,deltat_max) 
    return X

