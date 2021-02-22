import numpy as np

#compute a single euler step
def euler_step(dXdt,x0,t0,stepWidth):
    x1 = x0 + stepWidth*dXdt(x0,t0)
    return x1

# computes a single RK4 step
def RK4_step(f,x0,t0,h):
    k1 = f( x0          , t0       )
    k2 = f( x0 + h*k1/2 , t0 + h/2 )
    k3 = f( x0 + h*k2/2 , t0 + h/2 )
    k4 = f( x0 + h*k3   , t0 + h   )
    x1 = x0 + h*(k1 + 2*k2 + 2*k3 + k4)/6 
    return x1

#function uses whatever is smaller: h or deltat_max for getting from x1 to x2
def solve_to(dXdt,x0,t0,h,deltat_max,Method):
    if deltat_max < h:
        rem_dist = h
        X = x0
        T = t0
        if Method == 'Euler':
            while rem_dist > deltat_max:
                X = euler_step(dXdt,X,T,deltat_max)
                T += deltat_max
                rem_dist -= deltat_max
            X = euler_step(dXdt,X,T,rem_dist)
        elif Method == 'RK4':
            while rem_dist > deltat_max:
                X = RK4_step(dXdt,X,T,deltat_max)
                T += deltat_max
                rem_dist -= deltat_max
            X = RK4_step(dXdt,X,T,rem_dist)
    else:
        if Method == 'Euler':
            X = euler_step(dXdt,x0,t0,h)
        elif Method == 'RK4':
            X = RK4_step(dXdt,x0,t0,h)
    return X

def solve_ode(ode,x0,t,deltat_max,Method='Euler'):
    X = np.zeros((len(t),len(x0)))
    X[0] = x0
    for i in range(len(t)-1):
        h = t[i+1] - t[i] #if t given is not linearly spaced?
        X[i+1] = solve_to(ode,X[i],t[i],h,deltat_max,Method) 
    return X
