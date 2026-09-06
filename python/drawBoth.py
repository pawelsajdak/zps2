#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

outputDir = "plots"
dataDir = "../build/"

# Początkowa odległość (start w periastronie)
distanceInit = 746600.0

######## Dane z pierwszego pliku (2PN)
fileName1 = "out2PN_1.txt"
dataOrig1 = np.loadtxt(dataDir+fileName1, skiprows=3)

data1 = dataOrig1[dataOrig1[:,0] < 0]  # chcemy tylko minima odległości, a są one zapisywane z ujemnym czasem

times1 = -data1[:,0]      # czasy były zapisane jako ujemne
distances1 = data1[:,1]

# Przeskalowanie czasów
times1 = 1.e-9 * times1

# Odchylenia odległości minimalnych od początkowej wartości
distanceDevs1 = distances1 - distanceInit

######## Dane z drugiego pliku (2,5PN)
fileName2 = "out25PN_1.txt"
dataOrig2 = np.loadtxt(dataDir+fileName2, skiprows=3)

data2 = dataOrig2[dataOrig2[:,0] < 0]  # chcemy tylko minima odległości, a są one zapisywane z ujemnym czasem

times2 = -data2[:,0]      # czasy były zapisane jako ujemne
distances2 = data2[:,1]

# Przeskalowanie czasów
times2 = 1.e-9 * times2

# Odchylenia odległości minimalnych od początkowej wartości
distanceDevs2 = distances2 - distanceInit

########## Rysowanie #####################
# Rysowanie co n-tego punktu
n = 10

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(times1[::n], distanceDevs1[::n], s=0.1, color='darkorange',label='Rząd 2PN')
ax.scatter(times2[::n], distanceDevs2[::n], s=0.1, color='blue',label='Rząd 2,5PN')
ax.axhline(y=0, color='k', linestyle='--', alpha=0.5)
ax.set_xlabel(r'Czas [$10^9$ s]',fontsize=12)
ax.set_ylabel('Odchylenie separacji w periastronie [km]',fontsize=12)
ax.set_ylim(-0.005,0.001)
ax.set_title('Zmiany separacji obiektów w periastronie względem początkowej wartości',fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(fontsize=14,markerscale=30.0,loc='center right')

fig.savefig(os.path.join(outputDir, "both.pdf"), bbox_inches='tight')
plt.close()