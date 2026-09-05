#!/usr/bin/python3
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Wersja odpowiednia do symulacji zapisującej tylko ekstrema (wersja main.cpp)

args = sys.argv

outputDir = "devs"
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


arr = np.array(minDistances)
deviation = float(np.sqrt(np.mean((arr[1:] - arr[0])**2))) if len(arr) > 1 else 0.0

with open(os.path.join(outputDir,fileName),'w') as f_out:
    f_out.write(str(header)+"\n")
    f_out.write(f"Number of minimums: {len(minDistances)} \n")
    f_out.write(f"Standard deviation of the minimum distance: {deviation}")