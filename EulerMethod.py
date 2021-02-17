import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from OdeSolver import solve_ode

def our_ode(x,t):
    dxdt = x
    return dxdt

#initial condition
x0 = 1
t = np.linspace(0,10,200)
x = odeint(our_ode,x0,t)
X = solve_ode(our_ode,x0,t,2**-3,'Euler')
X2 = np.exp(t)
plt.figure(1)
plt.plot(t,x)
plt.plot(t,X)
plt.plot(t,X2)
plt.show()

#compute error \/
timestep = np.logspace(-7,1,200,base=2.0)
Eul_err = np.zeros(len(timestep))
RK_err = np.zeros(len(timestep))

for i in range(len(timestep)):
    Eul_err[i] = abs(solve_ode(our_ode,x0,t,timestep[i],'Euler')[-1] - np.exp(timestep[i]))
    RK_err[i] = abs(solve_ode(our_ode,x0,t,timestep[i],'RK4')[-1] - np.exp(timestep[i]))
plt.figure(2)
plt.loglog(timestep,Eul_err)
plt.loglog(timestep,RK_err)
plt.show()
 