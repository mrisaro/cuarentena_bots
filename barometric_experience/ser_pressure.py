#!/usr/bin/python
import time, serial, sys
import numpy as np
import matplotlib.pyplot as plt
import datetime
import os.path
ser = serial.Serial('/dev/ttyACM0', 9600)
var = [b'P']

act = input("Ingrese acción (medir/fin/guardar)")

fig = plt.figure(1,figsize=(10,6))
ax = fig.add_subplot(111)
pr  = []
dp  = []
pi  = []
piso = 0
ii   = 0

while(act=='m'):
    a = []

    for j in range(20):
        ser.write(var[0])
        val=float(ser.readline())
        print(val)
        a.append(val)
        ax.plot(ii,val,'.',color='C0',markersize=10)
        plt.show(block=False)
        ii = ii+1
        plt.pause(0.1) # pause
        time.sleep(2)

    act = input("Ingrese acción (medir/fin/guardar)")
    pr.append(np.mean(a))
    dp.append(np.std(a))
    pi.append(piso)
    piso = piso+1

act = input("Ingrese acción (medir/fin/guardar)")

if (act=='g'):
    A = [pi, pr, dp]
    A = np.transpose(A)
    file = 'data.csv'
    np.savetxt(file, A, header="I,P(hPa),dP(hPa)", fmt="%1.3f",
					delimiter=',', comments='')
