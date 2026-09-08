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
import sys

# Program do analizy wyników programu symulacyjnego "main"
# Przy wywołaniu należy podać nazwę pliku z wynikami znajdującego się w folderze "build"

# Program wybiera minima r, czyli te z ujemnym czasem
# Do rozkładu r(t) dopasowywana jest prosta 
# Rysowany jest wykres r(t) oraz dopasowana prosta

args = sys.argv

outputDir = "plots"
dataDir = "../build/"
fileName = ""
if len(sys.argv) > 1:
    fileName = str(args[1])
else:
    exit()
dataOrig = np.loadtxt(dataDir+fileName, skiprows=3)

data = dataOrig[dataOrig[:,0] < 0]  # chcemy tylko minima odległości, a są one zapisywane z ujemnym czasem

times = -data[:,0]      # czasy były zapisane jako ujemne
distances = data[:,1]

# Początkowa odległość (start w periastronie)
distanceInit = 746600.0

# Odchylenia odległości minimalnych od początkowej wartości
distanceDevs = distances - distanceInit

######## Dopasowanie prostej #######
slope, intercept = np.polyfit(times, distanceDevs, 1)

text = f"Parametry prostej:\nnachylenie [km/s]: {slope:.2e}\nwyraz wolny [km]: {intercept:.2e}"

# Rysowanie co n-tego punktu
n = 10
times = times[::n]
distanceDevs = distanceDevs[::n]

linePoints = slope * times + intercept

# Przeskalowanie czasów
times = 1.e-9 * times

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(times, distanceDevs, s=0.1, color='blue')
ax.axhline(y=0, color='k', linestyle='--', alpha=0.5)
ax.plot(times, linePoints, color='red', linewidth=0.4)
ax.set_xlabel(r'Czas [$10^9$ s]',fontsize=12)
ax.set_ylabel('Odchylenie separacji w periastronie [km]',fontsize=12)
ax.set_ylim(-0.005,0.001)
ax.set_title('Zmiany separacji obiektów w periastronie względem początkowej wartości',fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)

bbox_props = dict(
    boxstyle="round,pad=0.5",  
    facecolor="wheat",         
    edgecolor="black",         
    alpha=0.5                  
)

ax.text(
    0.05, 0.3,               
    text, 
    transform=ax.transAxes, 
    fontsize=11,
    linespacing=1.8,
    verticalalignment='top',
    bbox=bbox_props
)

fig.savefig(os.path.join(outputDir, fileName[:-4]+"Fit.pdf"), bbox_inches='tight')
plt.close()