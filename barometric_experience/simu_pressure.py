import numpy as np
import matplotlib.pyplot as plt

def pr_atm(h,p0,g,M,T0,R0):
    p = p0*np.exp(-g*h*M/T0/R0)
    return p

#parametros
p0 = 1013.25        # atmospheric pressure in hPa
g  = 9.8            # gravity
T0 = 288.16         # sea Temperature
M  = 0.0298         # Molar mass of dry (kg/mol)
R0 = 8.314          # Universal gas constant (J/mol/K)

N = 500
h = np.linspace(0,3*15,N)
p = pr_atm(h,p0,g,M,T0,R0)

fig = plt.figure(1,figsize=(10,6))
ax = fig.add_subplot(111)
ax.plot(p,h,'--',linewidth=2)
ax.set_xlabel('Altura (m)')
ax.set_ylabel('Presión (hPa)')
ax.grid(linestyle='--')
fig.tight_layout()
plt.savefig('simu_pressure.png')
