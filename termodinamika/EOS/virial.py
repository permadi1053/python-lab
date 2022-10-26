#permadi-lab
#import module matematika math
import math

print("selamat datang di permadi-lab.............")
nama = input("siapa nama kamu?")
print(
  "hallo " + nama +
  " selamat datang di solver untuk menghitung faktor kompresibilitas gas non ideal dengan menggunakan persamaan virial"
)
komponen = input("apa nama komponennya? ")
print("isi parameter berikut: ")
print("varibel: ")
T = int(input("T (K)= "))
P = int(input("P (bar)= "))
print("konstanta: ")
Tc = int(input("Tc (K)= "))
Pc = int(input("Pc (bar)= "))
Tr = (T / Tc)
Pr = (T / Pc)
w = float(input("w = "))
print("maka")
print("Tr = " + str(Tr) + " Pr = " + str(Pr) + " w = " + str(w))
R = 0.08206
B0 = 0.083 - 0.422 / (float(Tr)**1.6)
B1 = 0.139 - 0.172 / (float(Tr)**4.2)
print("B0 = " + str(B0))
print("B1 = " + str(B1))
B = R * Tc * (B0 + (w * B1)) / Pc
print("B  = " + str(B))
z = 1 + B * P / (R * T)
v = R * z * T / P
print("maka faktor kompresibilitas (z) dan volum molar (v) " + komponen +
      " adalah:")
print("z = " + str(z))
print("v = " + str(v) + " L/gmol")
print("terimakasih " + nama +
      " sudah menggunaan volver ini, semoga bermanfaat")
