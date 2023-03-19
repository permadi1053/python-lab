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
Ca0 = 18.85; #mol/m^3
To = 1035; #K
Tr = 298.15 #K 
dH = 80770; #J/mol 
Da = 6.8; #delta n
Db = -(5.7E-3) #delta b
Dc = -(1.27E-6) #delta c
Fa0 = 37.6; #mol/s
def ODEfun(Yfuncvec, V, Ca0,To,Tr,dH,Da,Db,Dc,Fa0):
    X= Yfuncvec[0]
    T= Yfuncvec[1]
    #Explicit Equation Inline
    FA = Fa0*(1-X);
    FB = Fa0*X;
    FC = Fa0*X;
    CPA = 26.83 + 0.183*T - 45.86E-6*T**2;
    CPB = 20.04 + 0.0945*T - 30.95E-6*T**2;
    CPC = 13.39 + 0.077*T - 18.71E-6*T**2;
    k = 8.2E14*np.exp(-34222/T);
    ra = -k*Ca0*(1-X)*(To/T)/(1+X);
    DHrxn = dH + Da*(T-Tr) + (Db/2)*(T**2-Tr**2) + (Dc/3)*(T**3-Tr**3);
     # Differential equations
    dXdV = - ra / Fa0; 
    dTdV = -ra*(-DHrxn)/(FA*CPA + FB*CPB + FC*CPC);
    return (dXdV,dTdV)

Vspan = np.linspace(0, 1, 100) # Range for the independent variable
y0 = np.array([0,1035]) # Initial values for the dependent variables

#%%
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
plt.subplots_adjust(left  = 0.37)
fig.subplots_adjust(wspace=0.25,hspace=0.3)
fig.suptitle("""                                         Produksi Asetat Anhidrid (PFR)(Adiabatis)""", fontweight='bold', x = 0.22)

sol = odeint(ODEfun, y0, Vspan, (Ca0,To,Tr,dH,Da,Db,Dc,Fa0))
X = sol[:, 0]
T = sol[:,1]
k = 8.2E14*np.exp(-34222/T);
Xe = k / (1 + k); 
ra = -k*Ca0*(1-X)*(To/T)/(1+X); 
rate = 0 - ra; 

p1= ax2.plot(Vspan,T)[0]
ax2.legend(['T'], loc='upper right')
ax2.set_xlabel(r'$Volume  {(m^3)}$', fontsize='medium')
ax2.set_ylabel('Temperature (K)', fontsize='medium')
ax2.set_ylim(700,1100)
ax2.set_xlim(0,0.1)
ax2.grid()

p2,p4 = ax3.plot(Vspan,X,Vspan,Xe)
ax3.legend(['X','$X_e$'], loc='upper right')
ax3.set_ylim(0,1)
ax3.set_xlim(0,1)
ax3.grid()
ax3.set_xlabel(r'$Volume  {(m^3)}$', fontsize='medium')
ax3.set_ylabel('Conversion', fontsize='medium')

p3 = ax4.plot(Vspan, rate)[0]
ax4.legend(['$-r_A$'], loc='upper right')
ax4.set_ylim(0,100)
ax4.set_xlim(0,1)
ax4.grid()
ax4.set_xlabel(r'$Volume  {(m^3)}$', fontsize='medium')
ax4.set_ylabel('$Rate {(mol/ m^3.s)}$', fontsize='medium')

ax1.axis('off')
axcolor = 'black'
ax_Ca0 = plt.axes([0.32, 0.80, 0.2, 0.015], facecolor=axcolor)
ax_To = plt.axes([0.32, 0.75, 0.2, 0.015], facecolor=axcolor)
ax_dH = plt.axes([0.32, 0.70, 0.2, 0.015], facecolor=axcolor)


sCa0 = Slider(ax_Ca0, r'C$_{A0}$($\frac{kmol}{m^3}$)', 1, 100, valinit=18.85,valfmt='%1.1f')
sTo = Slider(ax_To, 'T$_{0}$ ($K$)', 300, 1500, valinit=1035,valfmt='%1.0f')
sdH= Slider(ax_dH, r'$\Delta H_{Rx}^\circ$ ($\frac{J}{mol}$)', 50000, 100000, valinit=80770,valfmt='%1.0f')


def update_plot2(val):
    Ca0 = sCa0.val
    To =sTo.val
    dH =sdH.val
    sol = odeint(ODEfun, y0, Vspan, (Ca0,To,Tr,dH,Da,Db,Dc,Fa0))
    X = sol[:, 0]
    T = sol[:,1]
    k = 8.2E14*np.exp(-34222/T);
    Xe = k / (1 + k); 
    ra = -k*Ca0*(1-X)*(To/T)/(1+X); 
    rate = 0 - ra;    
    p1.set_ydata(T)
    p2.set_ydata(X)
    p4.set_ydata(Xe)
    p3.set_ydata(rate)
    fig.canvas.draw_idle()
    
sCa0.on_changed(update_plot2)
sTo.on_changed(update_plot2)
sdH.on_changed(update_plot2)


resetax = plt.axes([0.37, 0.86, 0.12, 0.065])
button = Button(resetax, 'Reset variables', color='cornflowerblue', hovercolor='0.975')

def reset(event):
    sCa0.reset()
    sTo.reset()
    sdH.reset()


button.on_clicked(reset)
