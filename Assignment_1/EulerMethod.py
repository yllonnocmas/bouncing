import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from NewOdeSolver import solve_ode
from NewOdeSolver import euler_step

def our_ode(X,t):
    dx1dt = X[1]
    dx2dt = -X[0]
    return np.array([dx1dt,dx2dt])

def HIV(x,t):
    kr1 = 1e5
    kr2 = 0.1
    kr3 = 2e-7
    kr4 = 0.5
    kr5 = 5
    kr6 = 100
    h = x[0]
    i = x[1]
    v = x[2]
    p = kr3*h*v
    dhdt = kr1 - kr2*h - p
    didt = p - kr4*i
    dvdt = -p -kr5*v + kr6 *i
    return np.array([dhdt,didt,dvdt])


plt.figure(1)

'''
#plot actual e^t - analytical solution
t = np.linspace(0,1,500)
X = np.exp(t)
plt.plot(t,X,label='$x(t) = e^{t}$')
'''

#initial condition & max stepwidth either h or deltat_max whatever is smaller
x0 = np.array([0.5,0.5])
deltat_max = 2**-10
t = np.linspace(0,2*np.pi,100)
X = odeint(our_ode,x0,t)
#Euler Method
X = solve_ode(our_ode,x0,t,deltat_max,'Euler')

plt.plot(X[:,0],X[:,1])
plt.show()
plt.figure(2)
plt.plot(t,X[:,0],label='x')
plt.plot(t,X[:,1],label='y')
plt.show()

'''
print('Euler  = ',X[-1])
plt.plot(t,X[0],label='Euler Method x dot',linestyle='-.')
plt.plot(t,X[1],label='Euler method y dot'linestyle='+')
'''

'''
#RK4 Method
X = solve_ode(our_ode,x0,t,deltat_max,'RK4')
print('RK4    = ',X[-1])
plt.plot(t,X,label='RK4',linestyle='--')
plt.legend(loc='best')
plt.show()
print('exp(1) = ',np.exp(1))
'''

'''
plt.figure(2)
#compute errors
t = np.linspace(0,1,50)
timestep = np.logspace(-5,-2,300)
Eul_err = np.zeros(len(timestep))
RK_err = np.zeros(len(timestep))
for i in range(len(timestep)):
    Eul_err[i] = abs(solve_ode(our_ode,x0,t,timestep[i],Method='Euler')[-1]  - np.exp(1) )
    RK_err[i]  = abs(solve_ode(our_ode,x0,t,timestep[i],Method='RK4')[-1]    - np.exp(1) )


plt.loglog(timestep,Eul_err,label="Euler's Method")
plt.loglog(timestep,RK_err,label='RK4 Method')
plt.legend(loc='best')
plt.xlabel('$\\Delta t_{Max}$')
plt.ylabel('Absolute Error')
plt.show()
'''
