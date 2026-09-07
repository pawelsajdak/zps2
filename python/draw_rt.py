#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# Wersja odpowiednia do symulacji zapisującej tylko ekstrema (wersja main.cpp)
# Program wybiera minima r, czyli te z ujemnym czasem
# Rysowany jest wykres r(t)

args = sys.argv

outputDir = "plots"
dataDir = "../build/"
fileName = ""
if len(sys.argv) > 1:
    fileName = str(args[1])
else:
    exit()
header = np.loadtxt(dataDir+fileName, skiprows=1, max_rows=1)
dataOrig = np.loadtxt(dataDir+fileName, skiprows=3)

data = dataOrig[dataOrig[:,0] < 0]  # chcemy tylko minima odległości, a są one zapisywane z ujemnym czasem

# Uwzględnianie co n-tego punktu
n = 10
data = data[::n,:]

times = -data[:,0]      # czasy były zapisane jako ujemne
distances = data[:,1]

# Początkowa odległość (start w periastronie)
distanceInit = 746600.0

# Odchylenia odległości minimalnych od początkowej wartości
distanceDevs = distances - distanceInit

plt.figure(figsize=(8, 5))
plt.scatter(times, distanceDevs, s=0.1)
plt.axhline(y=0, color='k', linestyle='--', alpha=0.5)
plt.xlabel('Czas [s]')
plt.ylabel('Odchylenie separacji w periastronie [km]')
plt.title('Zmiany separacji obiektów w periastronie względem początkowej wartości')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig(os.path.join(outputDir, fileName[:-4]+".pdf"), bbox_inches='tight')
plt.close()
