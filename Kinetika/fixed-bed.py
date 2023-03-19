#%%
#Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams.update({'font.size': 13, 'lines.linewidth': 2.5})
from matplotlib.widgets import Slider, Button

#%%
#Explicit equations
Ca0 = 0.271
Cpa = 40; #J/gmol.K
T0 = 450; #K
Ta = 500 #K 
Fa0 = 5; #gmol/menit
dH = -40000
def ODEfun(Yfuncvec, W, Ca0,Cpa,T0,Ta,dH,Fa0):
    X= Yfuncvec[0]
    T= Yfuncvec[1]
    P= Yfuncvec[2]
    #Explicit Equation Inline
    k = 0.5*np.exp(5032*(1/T0 - 1/T));
    temp = Ca0*(T0/T)*P/(1-0.5*X);
    Ca = temp*(1-X);
    Cc = temp*0.5*X;
    Kc = 25000*np.exp(dH/8.314*(1/T0-1-T));     
    ra = -k*(Ca*Ca-(Cc/Kc));
    # Differential equations
    dXdW = - ra / Fa0; 
    dTdW = (0.8*(Ta-T)+ra*dH)/(Cpa*Fa0)
    dPdW = -0.015*(1-0.5*X)*(T/T0)/(2*P)
    return (dXdW,dTdW,dPdW)

Wspan = np.linspace(0, 20, 100) # Range for the independent variable
y0 = np.array([0,450,1]) # Initial values for the dependent variables
sol = odeint(ODEfun, y0, Wspan, (Ca0,Cpa,T0,Ta,dH,Fa0))
X = sol[:,0]
T = sol[:,1]
P = sol[:,2]
k = 0.5*np.exp(5032*(1/T0 - 1/T))
temp = 0.271*(T0/T)*P/(1-0.5*X)
Ca = temp*(1-X)
Cc = temp*0.5*X
Kc = 25000*np.exp(dH/8.314*(1/T0-1-T))
ra = -k*(Ca*Ca-(Cc/Kc))
rate = 0 - ra;

fig, ((ax1,ax2,ax3),(ax4,ax5,ax6)) = plt.subplots(2,3)
plt.subplots_adjust(left  = 0.37)
fig.subplots_adjust(wspace=0.7,hspace=0.5)
fig.suptitle("""Simulasi Fixed-bed reaktor (adiabatis)""", fontweight='bold', x = 0.22)

p1 = ax2.plot(Wspan,rate)[0]
ax2.legend(['$-r_A$'], loc='best')
ax2.set_ylim(0,5)
ax2.set_xlim(0,20)
ax2.grid()
ax2.set_xlabel(r'$Katalis  {(Kg)}$', fontsize='medium')
ax2.set_ylabel(r'$Rate {(mol/ m^3.s)}$', fontsize='medium')

p2 = ax3.plot(Wspan,X)[0]
ax3.legend(['X'], loc='best')
ax3.set_ylim(0,1)
ax3.set_xlim(0,20)
ax3.grid()
ax3.set_xlabel(r'$Katalis  {(Kg)}$', fontsize='medium')
ax3.set_ylabel('Conversi', fontsize='medium')

p3 = ax4.plot(Wspan,P)[0]
ax4.legend(['$P$'], loc='best')
ax4.set_ylim(0,1.5)
ax4.set_xlim(0,20)
ax4.grid()
ax4.set_xlabel(r'$Katalis  {(Kg)}$', fontsize='medium')
ax4.set_ylabel('Pressure-Drop (atm)', fontsize='medium')

p4 = ax5.plot(Wspan,T)[0]
ax5.legend(['$T$'], loc='best')
ax5.set_ylim(300,1500)
ax5.set_xlim(0,20)
ax5.grid()
ax5.set_xlabel(r'$Katalis  {(Kg)}$', fontsize='medium')
ax5.set_ylabel('Temperature', fontsize='medium')

p5,p6= ax6.plot(Wspan,Ca,Wspan,Cc)
ax6.legend(['$Ca$','$Cc$'], loc='best')
ax6.set_ylim(0,0.5)
ax6.set_xlim(0,20)
ax6.grid()
ax6.set_xlabel(r'$Katalis  {(Kg)}$', fontsize='medium')
ax6.set_ylabel(r'$Konsentrasi {(g.mol/dm^3)}$', fontsize='medium')

ax1.axis('off')
axcolor = 'black'
ax_Ca0 = plt.axes([0.32, 0.80, 0.17, 0.015], facecolor=axcolor)
ax_Fa0 = plt.axes([0.32, 0.75, 0.17, 0.015], facecolor=axcolor)
ax_T0 = plt.axes([0.32, 0.70, 0.17, 0.015], facecolor=axcolor)


sCa0 = Slider(ax_Ca0, r'C$_{a0}$($\frac{g.mol}{dm^3}$)', 0, 1, valinit=0.271,valfmt='%1.1f')
sFa0= Slider(ax_Fa0, r'F$_{a0}$($\frac{g.mol}{menit}$)', 1, 20, valinit=5,valfmt='%1.0f')
sT0 = Slider(ax_T0, 'T$_{0}$ ($K$)', 200, 1000, valinit=450,valfmt='%1.0f')

def update_plot2(val):
    Ca0 = sCa0.val
    Fa0 =sFa0.val
    T0 =sT0.val
    sol = odeint(ODEfun, y0, Wspan, (Ca0,Cpa,T0,Ta,dH,Fa0))
    X = sol[:,0]
    T = sol[:,1]
    P = sol[:,2]
    k = 0.5*np.exp(5032*(1/T0 - 1/T))
    temp = 0.271*(T0/T)*P/(1-0.5*X)
    Ca = temp*(1-X)
    Cc = temp*0.5*X
    Kc = 25000*np.exp(dH/8.314*(1/T0-1-T))
    ra = -k*(Ca*Ca-(Cc/Kc))
    rate = 0 - ra;
    p1.set_ydata(rate)
    p2.set_ydata(X)
    p3.set_ydata(P)
    p4.set_ydata(T)
    p5.set_ydata(Ca)
    p6.set_ydata(Cc)
    fig.canvas.draw_idle()
    
sCa0.on_changed(update_plot2)
sFa0.on_changed(update_plot2)
sT0.on_changed(update_plot2)


resetax = plt.axes([0.37, 0.86, 0.12, 0.065])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sCa0.reset()
    sFa0.reset()
    sT0.reset()


button.on_clicked(reset)
