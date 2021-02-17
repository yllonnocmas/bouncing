import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from OdeSolver import solve_ode

def our_ode(x,t):
    dxdt = x
    return dxdt

#initial condition
x0 = 1
t = np.linspace(0,5)
x = odeint(our_ode,x0,t)
X = solve_ode(our_ode,x0,t,2**-3,'Euler')
plt.plot(t,x)
plt.plot(t,X)

plt.show()
 