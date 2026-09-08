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
import numpy as np
import matplotlib.pyplot as plt
import os

# Skrypt do stworzenia wykresu ze średnią kwadratową odchyleń dla różnych kroków czasowych (2PN)

x = ["1","0.1","0.01","0.001"]
y = [2.31721e-02, 2.30481e-04, 2.53821e-06, 6.52508e-06]

plt.scatter(x,y)
plt.xlabel("Krok czasowy [s]")
plt.ylabel("Średnia kwadratowa odchylenia [km]")
plt.yscale('log')
plt.title("Odchylenie kolejnych odległości w periastronie\n od początkowej wartości\n przy poprawkach do rzędu 2PN")

plt.savefig("krokCzasowy_e7.pdf", format='pdf', bbox_inches='tight')
plt.close()