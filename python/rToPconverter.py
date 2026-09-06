#!/usr/bin/python3
import sys
import numpy as np

if len(sys.argv) < 2:
    exit()

rDot = sys.argv[1]
rDot = float(rDot)

G = 1.327 * 1.e11       # km^3 / Mo / s^2
M = 1.4414 + 1.3867     # Mo (solar masses)
ecc = 0.62
P = 0.323 * 24 * 3600   # s

# Pdot = (6*rDot/(1-ecc)) * np.cbrt( (np.pi*np.pi*P)/(16*G*M) )

# A = 1.5*( (4pi^2P)/(GM) )^(1/3)
A = (4*np.pi**2 * P) / (G*M)
A = np.cbrt(A)
A *= 1.5
    
B = 1 + (73/24) * ecc**2 + (37/96) * ecc**4

# licznik ułamka
C = (64/5)*B / (1-ecc**2)

# mianownik
D = (64/5) * (B/(1 + ecc)) - (304/15) * ecc - (121/15) * ecc**3

# końcowe obliczenie
Pdot = A * rDot * ( C/D )

print(f"rDot = {rDot:.2e} \nPdot = {Pdot:.2e}")