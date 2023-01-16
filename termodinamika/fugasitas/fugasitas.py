import matplotlib.pyplot as plt
import numpy as np
import math
import time


print("selamat datang di permadi-lab.............")
nama = input("siapa nama kamu?")

print("hallo " + nama + " selamat datang di solver untuk mengestimasi Fugasitas dan Koefisien Fugasitas dengan menggunakan persamaan Virial")

print ("Program berjalan\n")
input("Tekan [Enter] untuk memulai…")

for i in range(3, 0, -1):
    time.sleep(1)
    print (str(i))


print('state: fluid state(V: vapor)')
print('eos: equation of state (VR)')
print('P: pressure(bar)')
print('T: temperature(K)')
print('Tc,Pc: critical T(K) and P(bar)')
print('w: acentric factor')
print('output:')
print('phig: fugacity coefficient')
print('f: fugacity (bar)')
print('Tr and Pr (reduced T and P)')

komponen = input("apa nama komponennya? ")
print("masukkan parameter berikut : ") 
T = float(input('T = '))
P = float(input('P= '))
Tc = float(input('Tc = '))
Pc = float(input('Pc = '))
w = float(input('w = '))      
Tr = T/Tc
Pr = P/Pc
R = 83.14 #cm^3*bar/mol/K


#parameter EOS virial
al = 1
sm = 0
ep = 0
om = 0.125
ps = 0.42188
kappa = 0
#compressibility factor (Z)
beta = om*Pr/Tr
q = ps*al/(om*Tr) # beta and q
B0 = 0.083 - 0.422/(Tr**1.6)
B1 = 0.139 - 0.172/(Tr**4.2)
B = R*Tc*(B0 + w*B1)/Pc
Z = 1 + B*P/(R*T)
V = Z*R*T/P #cm^3/mol
#fugacity coefficient
a = ps*al*R**2*Tc**2/Pc
b = om*R*Tc/Pc # a, b
qi = a/(b*R*T) 
Bd = b*P/(R*T) # A, B
phig = math.exp(Z-1-math.log(Z*(1-b/V))-a/(R*T*V))
f = phig*P


print ("Tunguu......")
for i in range(3, 0, -1):
    time.sleep(1)
    print (str(i))
    
print ("hasil")    
print("Tr = " + str(Tr) + " Pr = " + str(Pr) + " w = " + str(w))    
print("Maka faktor kompresibilitas (z) dan volum molar (v) " + komponen +" adalah:")
print("Z = " + str(Z))
print("V = " + str(V) + " cm^3/mol")
print ("dan")
print ("============================================================")
print("Koefisien fugasitas = " + str(phig))
print("Fugasitas = " + str(f) + " Bar")
print("Terimakasih " + nama + " telah menggunaan solver ini, semoga bermanfaat")
