#!/usr/bin/python3
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Skrypt szuka minimow odleglosci w kolejnych przedzialach czasowych postaci [t+TExp/2, t+1.5*TExp],
# gdzie t jest czasem ostatniego znalezionego minimum.
# Na koncu wypisywane sa znalezione minima odleglosci oraz czasy ich wystapienia
# Poza tym obliczane jest odchylenie kwadratowe minimalnych odleglosci od zerowej (dokladnej) wartosci

args = sys.argv

outputDir = "devs"
dataDir = "../build/"
fileName = ""
if len(sys.argv) > 1:
    fileName = str(args[1])
else:
    fileName = "out.txt"
header = np.loadtxt(dataDir+fileName, skiprows=1, max_rows=1)
data = np.loadtxt(dataDir+fileName, skiprows=3)

times = data[:,0]
distances = data[:,1]
endTime = times[-1]

TExp = 7.75*3600    # spodziewany okres orbity
t = 0               # zmienna robocza

timesOfMin = [times[0]]     
minDistances = [distances[0]]
# Symulacja zaczyna się w periastronie

while (t+TExp < endTime):
    tUp = min(t+1.5*TExp, endTime)
    start_index = int(np.argmax(times > t+TExp/2))
    end_index   = int(np.argmax(times >= tUp))
    if end_index <= start_index: break
    
    seg = distances[start_index:end_index]
    minIdx = int(np.argmin(seg))
    minDistance = float(seg[minIdx])
    timeOfMin   = float(times[start_index + minIdx])
    
    timesOfMin.append(timeOfMin)
    minDistances.append(minDistance)

    t = timeOfMin

arr = np.array(minDistances)
deviation = float(np.sqrt(np.mean((arr[1:] - arr[0])**2))) if len(arr) > 1 else 0.0

with open(os.path.join(outputDir,"Full10"+fileName),'w') as f_out:
    f_out.write(str(header)+"\n")
    f_out.write(f"Number of minimums: {len(minDistances)} \n")
    f_out.write(f"Standard deviation of the minimum distance: {deviation}")