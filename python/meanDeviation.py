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
# Obliczana jest średnia kwadratowa odchylenia r od wartości początkowej

args = sys.argv

outputDir = "devs"
dataDir = "../build/"
fileName = ""
if len(sys.argv) > 1:
    fileName = str(args[1])
else:
    exit()
header = np.loadtxt(dataDir+fileName, skiprows=1, max_rows=1)   # parametry symulacji
dataOrig = np.loadtxt(dataDir+fileName, skiprows=3)

data = dataOrig[dataOrig[:,0] < 0]  # chcemy tylko minima odległości, a są one zapisywane z ujemnym czasem
data = data[data[:,0] >= -1.e7]      # w celu porównania, tylko czas do 10^7 s (czasy są tu ujemne)

times = -data[:,0]      # czasy były zapisane jako ujemne
distances = data[:,1]

# Początkowa odległość (start w periastronie)
distanceInit = 746600.0

# Odchylenia odległości minimalnych od początkowej wartości
distanceDevs = distances - distanceInit

# Obliczenia średniej kwadratowej
arr = np.array(distanceDevs)
quadMean = float( np.sqrt( np.mean(arr**2) ) )

with open(os.path.join(outputDir,"e7"+fileName),'w') as f_out:
    f_out.write(f"Ostatni czas: {times[-1]:.2e} \n")
    f_out.write("całkowity czas \t krok czasowy \t liczba kroków \t to2PN? \n"+str(header)+"\n")
    f_out.write(f"Liczba minimów: {len(distances)} \n")
    f_out.write(f"Średnia kwadratowa odchyleń r: {quadMean:.5e}")

print(f"Ostatnie odchylenie: {distanceDevs[-1]:.2e}")