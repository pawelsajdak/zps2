'''
  * Copyright (c) 2026 Paweł Sajdak, Franciszek Drągowski
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
  *
  * This program is distributed in the hope that it will be useful,
  * but WITHOUT ANY WARRANTY; without even the implied warranty of
  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  * GNU General Public License for more details.
  *
  * You should have received a copy of the GNU General Public License
  * along with this program. If not, see <https://www.gnu.org/licenses/>.
'''

#!/usr/bin/python3
import sys
import numpy as np

# Program służący do obliczania tempa zaniku okresu orbitalnego (\dot{P}) na podstawie tempa zaniku separacji w periastronie (\dot{r_p})
# Przy wywołaniu należy podać wartość \dot{r_p}

if len(sys.argv) < 2:
    exit()

rDot = sys.argv[1]
rDot = float(rDot)

G = 1.327 * 1.e11       # km^3 / Mo / s^2
M = 1.4414 + 1.3867     # Mo (solar masses)
ecc = 0.62
P = 0.323 * 24 * 3600   # s


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