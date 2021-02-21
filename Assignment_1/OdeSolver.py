import numpy as np

#compute a single euler step
def euler_step(f,x0,t0,stepWidth):
    x1 = x0 + stepWidth*f(x0,t0)
    return x1

#compute a single RK4 step
def RK4_step(f,x0,t0,h):
    k1 = f( x0          , t0       )
    k2 = f( x0 + h*k1/2 , t0 + h/2 )
    k3 = f( x0 + h*k2/2 , t0 + h/2 )
    k4 = f( x0 + h*k3   , t0 + h   )
    x1 = x0 + h*(k1 + 2*k2 + 2*k3 + k4)/6 
    return x1

#solves from x1,t1 to x2,t2 in steps no bigger than deltatmax
#deltamax should be powers of 2 to reduce rounding error?
#h is width between plotting values of ode
def solve_to(dxdt,x1,t1,h,deltat_max,Method):
    
    if deltat_max < h:
        deltatmaxSteps = int(h/deltat_max)          # gives number of delta t_max steps
        r_step = h - (deltatmaxSteps*deltat_max)    # remainder step width - just 1 step
        X = np.zeros(deltatmaxSteps + 1)            # create arrays of X and t values initialized with x1 and t1
        T = np.zeros(deltatmaxSteps + 1) 
        X[0] = x1
        T[0] = t1
        if Method == 'Euler':
            for i in range(deltatmaxSteps):
                X[i+1] = euler_step(dxdt,X[i],T[i],deltat_max)
                T[i+1] = T[i] + deltat_max
            X = np.append(X,euler_step(dxdt,X[-1],T[-1],r_step))
            
        
        elif Method == 'RK4':
            for i in range(deltatmaxSteps):
                X[i+1] = RK4_step(dxdt,X[i],T[i],deltat_max)
                T[i+1] = T[i] + deltat_max
            X = np.append(X,RK4_step(dxdt,X[-1],T[-1],r_step))
        x2 = X[-1]
    else:
        
        if Method == 'Euler':
            x2 = euler_step(dxdt,x1,t1,h)
        elif Method == 'RK4':
            x2 = RK4_step(dxdt,x1,t1,h)    
    return x2

#t is list/array of times to be plotted
def solve_ode(ode,x0,t,deltat_max,Method='Euler'):
    X = np.zeros(len(t))
    X[0] = x0
    for i in range(len(t)-1):
        h = t[i+1] - t[i] #if t given is not linearly spaced soucre of error?
        X[i+1] = solve_to(ode,X[i],t[i],h,deltat_max,Method) 
    return X

