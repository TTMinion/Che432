# Solving ODEs
# Considering batch reactor A -> B
#dCa/dt = -kCa; Ca0=10
#dCb/dt = kCa; Cb0 = 0

from scipy.integrate import odeint # this is basically the same  as ode 45 in mathlab
import numpy as np
import matplotlib.pyplot as plt




def equation (t, C):

    k1=1.08E-3
    k2=1.19E-3
    k3=1.59E-3
    P=110
    R=8.314
    Ta=683

    # Ca = x[0]
    # Cb = x[1.45]
    # Cc = x[0.99]
    
    cR0 = 0
    cS0 = 0
    cA0 = P/(R*Ta)

    dcAdt = -k1*cA0
    dcRdt = k1*cA0 - k2*cR0 - k3*cR0*cS0
    dcSdt = k2*cR0 + k3*cR0*cS0

    return dcAdt, dcRdt, dcSdt

t= np.linspace(0, 1500)
initial = [0.0193,0,0]
solution = odeint(equation, initial, t)

dcAdt = solution[:,0]
dcRdt = solution[:,1]
dcSdt = solution[:,2]

print(solution)
 
plt.figure()
plt.plot(t, dcAdt)
plt.plot(t,dcRdt)
plt.plot(t, dcSdt)
plt.title('Concetration vs Time @ T = 410 C')
plt.xlabel('Time')
plt.ylabel('Concentration')

plt.legend(loc='best')
plt.grid()
plt.show()
