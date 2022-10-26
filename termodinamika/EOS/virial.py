#permadi-lab
#import module matematika math
import math

print("selamat datang di permadi-lab.............")
nama = input("siapa nama kamu?")
print(
    "hallo " + nama +
    " selamat datang di solver untuk menghitung densitas gas non ideal dengan menggunakan persamaan virial"
)
komponen = input("apa nama komponennya? ")
print("isi parameter berikut: ")
print("varibel: ")
M = int(input("massa (Kg) = "))
BM = int(input("Berat molekut (Kg/Kmol) = "))
T = int(input("T (K)= "))
P = int(input("P (atm)= "))
print("konstanta: ")
Tc = int(input("Tc (K)= "))
Pc = int(input("Pc atm= "))
Tr = (T / Tc)
Pr = (T / Pc)
w = float(input("w = "))
print("maka")
print("Tr = " + str(Tr) + " Pr = " + str(Pr) + " w = " + str(w))
R = 0.0821  #m3 atm/kmol K
B0 = 0.083 - 0.422 / (float(Tr)**1.6)
B1 = 0.139 - 0.172 / (float(Tr)**4.2)
print("B0 = " + str(B0))
print("B1 = " + str(B1))
B = R * Tc * (B0 + (w * B1)) / Pc
print("B  = " + str(B))
z = 1 + B * P / (R * T)
v = R * z * T / P
print("faktor kompresibilitas (z) dan volum molar (v) " + komponen +
      " adalah:")
print("z = " + str(z))
print("v = " + str(v) + " m^3/Kmol")
print("maka densitas " + komponen + " adalah:")
m = M / BM
V = v * m
rho = M / V
print("m = " + str(m) + " Kmol")
print("V = " + str(V) + " m^3")
print("rho = " + str(rho) + " Kg/M^3")
print("terimakasih " + nama +
      " sudah menggunaan solver ini, semoga bermanfaat")
