import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#file = 'data_THL.csv'
file = 'data.csv'

df = pd.read_csv(file)
df2= pd.read_csv('presion.csv')

x = (10-df.I.values)*0.167*16
y = df.P.values
dy = df.dP.values


z = df2.Pr.values
med = np.arange(len(z))
mZ = np.zeros(len(z))
sZ = np.zeros(len(z))

for jj in range(11):
    ind = np.arange(20)+jj*20
    mZ[ind] = np.mean(z[ind])
    sZ[ind] = np.std(z[ind])


p,cov = np.polyfit(x, y, 1, cov=True)
g = 1.225/p[0]
x_fit = np.linspace(0,30,100)
y_fit = np.polyval(p,x_fit)

fig = plt.figure(1,figsize=(10,6))
ax = fig.add_subplot(111)
ax.errorbar(x, y, yerr=dy,fmt='.',markersize=20,color='C0',label='Datos Barómetro')
ax.plot(x_fit,y_fit,'--',color='C1',linewidth=2, label='Modelo Teórico')
ax.set_xlabel('Altura (m)',fontsize=15)
ax.set_ylabel('Presión (hPa)',fontsize=15)
ax.legend(fontsize=16)
ax.tick_params(labelsize=16)
ax.grid(linestyle='--')
fig.tight_layout()
#plt.savefig('data_experimento.png')

fig = plt.figure(2,figsize=(10,6))
ax = fig.add_subplot(111)
ax.plot(med,z,'.',markersize=6,label='Mediciones')
ax.plot(med,mZ,'--',color='C1',linewidth=2, label='Valor Medio')
ax.fill_between(med,mZ+sZ,mZ-sZ,color='C1',alpha=0.5, label='Std')
ax.set_xlabel('Medición (#)',fontsize=15)
ax.set_ylabel('Presión (hPa)',fontsize=15)
ax.legend(fontsize=16)
ax.tick_params(labelsize=16)
ax.grid(linestyle='--')
fig.tight_layout()
plt.savefig('data_individual.png')
