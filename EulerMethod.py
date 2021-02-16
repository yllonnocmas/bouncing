#function to compute a single euler step
def euler_step(dxdt,x0,t0,h):
    x1 = x0 + h*dxdt(x0,t0)
    return x1


def our_ode(x,t):
    dxdt = x
    return dxdt