#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# Wersja odpowiednia do symulacji zapisującej tylko ekstrema (wersja main.cpp)

args = sys.argv

outputDir = "plots"
dataDir = "../build/"
fileName = ""
if len(sys.argv) > 1:
    fileName = str(args[1])
else:
    exit()
header = np.loadtxt(dataDir+fileName, skiprows=1, max_rows=1)
data = np.loadtxt(dataDir+fileName, skiprows=3)

times = data[:,0]
distances = data[:,1]

timesOfMin = [0.0]     
minDistances = [746600.0]   # początkowa wartość

for i in range(len(times)):
    time = times[i]
    if time < 0:
        timesOfMin.append(time)
        minDistances.append(distances[i])

timeDiffs = [timesOfMin[i+1] - timesOfMin[i] for i in range(len(timesOfMin)-1)]

if len(timeDiffs) > 0:
    plt.figure(figsize=(8, 5))
    orbity = range(1, len(timeDiffs) + 1)
    plt.scatter(orbity, timeDiffs, label='Zmierzony okres orbitalny')
    plt.axhline(y=timeDiffs[0], color='k', linestyle='--', alpha=0.5, label='Okres referencyjny')
    plt.xlabel('Numer orbity')
    plt.ylabel('Okres orbitalny [s]')
    plt.title('Zmiany okresu orbitalnego')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    # plt.ylim(timeDiffs[0]-0.5*savingTimeInterval,timeDiffs[0]+0.5*savingTimeInterval)
    plt.savefig(os.path.join(outputDir, fileName[:-4]+".pdf"), bbox_inches='tight')
    plt.close()
    print("[SUKCES] Wygenerowano wykres")
