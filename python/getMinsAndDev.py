#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

# Skrypt szuka minimów odległości w kolejnych przedziałach czasowych postaci [t+TExp/2, t+1.5*TExp],
# gdzie t jest czasem ostatniego znalezionego minimum.
# Na końcu wypisywane są znalezione minima odległości oraz czasy ich wystąpienia
# Poza tym obliczane jest odchylenie kwadratowe minimalnych odległości od zerowej (dokładnej) wartości

dataFile = "../build/out.txt"
data = np.loadtxt(dataFile, skiprows=3)

times = data[:,0]
distances = data[:,1]
tStep = times[1] - times[0]
endTime = times[-1]

TExp = 7.75*3600    # expected orbital period
t = 0               # a working variable increased at the end of the "while" loop

timesOfMin = [times[0]]     
minDistances = [distances[0]]
# Added the first values, since the simulation begins at the minimum distance

while (t+TExp < endTime):
    tUp = min([t+1.5*TExp, endTime])
    start_index = np.argmax(times > t+TExp/2)
    end_index = np.argmax(times >= tUp)

    minDistance = np.min(distances[start_index:end_index])
    timeOfMin = times[start_index + np.argmin(distances[start_index:end_index])]
    
    timesOfMin.append(timeOfMin)
    minDistances.append(minDistance)

    t = timeOfMin

timeDiffs = [timesOfMin[i+1] - timesOfMin[i] for i in range(0,len(timesOfMin)-2)]
print([float(x) for x in timesOfMin])
print([float(x) for x in minDistances])
#print([float(x) for x in timeDiffs])

deviation = np.sqrt(np.mean((minDistances[1:] - minDistances[0])**2))
print(deviation)