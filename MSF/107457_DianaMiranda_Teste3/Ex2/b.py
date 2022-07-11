import matplotlib.pyplot as plt
import numpy as np

def acelera(t,x,vx):
    ax= g-g/vT **2*np.abs(vx)*vx
    return ax


def rk4(t,x,vx,dt):
    """
    Integração numérica de equação diferencial de 2ª ordem:
			d2x/dt2 = ax(t,x,vx)    com dx/dt= vx    de valor inicial
	Erro global:  proporcional a dt**4
    acelera=dvx/dt=Força(t,x,vx)/massa      : acelera é uma FUNÇÃO
    input:  t = instante de tempo
            x(t) = posição
            vx(t) = velocidade
            dt = passo temporal 
    output: xp = x(t+dt)
		    vxp = vx(t+dt)
    """
    ax1=acelera(t,x,vx)
    c1v=ax1*dt
    c1x=vx*dt
    ax2=acelera(t+dt/2.,x+c1x/2.,vx+c1v/2.)
    c2v=ax2*dt
    c2x=(vx+c1v/2.)*dt			# predicto:  vx(t+dt) * dt
    ax3=acelera(t+dt/2.,x+c2x/2.,vx+c2v/2.)
    c3v=ax3*dt
    c3x=(vx+c2v/2.)*dt
    ax4=acelera(t+dt,x+c3x,vx+c3v)
    c4v=ax4*dt
    c4x=(vx+c3v)*dt
      
    xp=x+(c1x+2.*c2x+2.*c3x+c4x)/6.
    vxp=vx+(c1v+2.*c2v+2.*c3v+c4v)/6.
    return xp,vxp

m = 1
k = 1
g=9.8
b= 0.05
beta = 0.001
f= 7.5
wf = 1.4

#Velocidade Terminal
vT = 6.8

t0 = 0
tf =300
dt = 0.001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)

x0= 2
vx0=4
x[0] = x0
v[0] = vx0


vxrk4 = np.empty(n)
xrk4 = np.empty(n)

vxrk4[0] = vx0
xrk4[0] = x0

arrayMaximos = []
temposMax = []
periodo = []

for i in range(n-1):  

    a[i] = (-k/m)*x[i]*(1+2*beta*x[i]**2)-(b*v[i])/m + f*np.cos(wf * t[i])/m
    #Euler
    v[i+1] = v[i] +a[i]*dt #a[i+1] - euler 
    x[i+1] = x[i] +v[i]*dt #v[i+1] - euler 

print("Vterm Euler  >",v[-1])


for i in range(n-1):
    
    if (t[i]>200 and x[i-1]<x[i]>x[i+1] and i>0 ): 
        arrayMaximos.append(x[i])
        temposMax.append(t[i])

for i in range(0,len(temposMax)-1):
    periodo.append(temposMax[i+1]-temposMax[i])


print("Periodo (s) ->",np.mean(periodo))
print("Amplitude (m) ->" ,np.mean(arrayMaximos))

plt.plot(t,x)
plt.grid()
plt.show()