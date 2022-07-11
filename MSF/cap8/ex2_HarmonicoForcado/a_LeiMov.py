import matplotlib.pyplot as plt
import numpy as np

#a) Calcule numericamente a lei do movimento, no caso em que a velocidade inicial é
#nula e a posição inicial 4 m. Tem confiança no seu resultado?

m = 1
k = 1
g=9.8

b=0.05 #kg
f=7.5 #N
wf=2 #rad/s

xeq = 0 

t0 = 0
tf =300
dt = 0.0001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)

x[0] = 4
v[0] = 0

a[0] = (-k*x[0] - b * v[0] + f*np.cos(wf*t[0]))/m

for i in range(n-1):   
    a[i+1] = (-k*x[i] - b * v[i] + f*np.cos(wf*t[i]))/m
    v[i+1] = v[i] +a[i+1]*dt 
    x[i+1] = x[i] +v[i+1]*dt
    

plt.plot(t,x)
plt.xlabel("t (s)")
plt.ylabel("x (m/s)")
plt.title("Oscilador Harmónico")
plt.show()

#Temos confiança, porque a lei do movimento obtida por dois passos temporais diferentes é a mesma. Como também os
#dois passo temporais produzem o mesmo resultado para o tempo final considerado