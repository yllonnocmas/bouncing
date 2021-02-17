import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from OdeSolver import solve_ode

def our_ode(x,t):
    dxdt = x
    return dxdt

#initial condition
x0 = 1
t = np.linspace(0,1)
print('t linspace is ',t)
X = solve_ode(our_ode,x0,t,1,'Euler')
print('Euler = ',X[-1])

plt.figure(1)
plt.plot(t,X,label='Euler Method')

X = solve_ode(our_ode,x0,t,1,'RK4')
print('RK4   = ',X[-1])
plt.plot(t,X,label='RK4')

print('exp(1)= ',np.exp(1))
'''
t = np.linspace(0,1,1000)
X = np.exp(t)
plt.plot(t,X,label='$x(t) = e^{t}$')
'''
plt.legend(loc='best')
plt.show()

plt.figure(2)
#compute errors
timestep = np.logspace(-5,0)
Eul_err = np.zeros(len(timestep))
RK_err = np.zeros(len(timestep))
for i in range(len(timestep)):
    Eul_err[i] = abs(solve_ode(our_ode,x0,t,timestep[i],Method='Euler')[-1]  - np.exp(1) )
    RK_err[i]  = abs(solve_ode(our_ode,x0,t,timestep[i],Method='RK4')[-1]    - np.exp(1) )


plt.loglog(timestep,Eul_err)
plt.loglog(timestep,RK_err)
plt.show()

'''
for i in range(len(timestep)):
    Eul_err[i] = abs(solve_ode(our_ode,x0,t,timestep[i],'Euler')[-1] - np.exp(timestep[i]))
    RK_err[i] = abs(solve_ode(our_ode,x0,t,timestep[i],'RK4')[-1] - np.exp(timestep[i]))


 '''