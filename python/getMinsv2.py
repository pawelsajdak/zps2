#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import os

dataDir = "../build/"
fileName = "out0.txt"
outputDir = "../getMins/"
os.makedirs(outputDir, exist_ok=True)

header = np.loadtxt(dataDir+fileName, skiprows=1, max_rows=1)

lines_data = []

with open(dataDir+fileName, "r", encoding="utf-8") as f:
    for _ in range(3):
        next(f, None) # pomiń pierwsze linie
    for line in f:
        clean_line = line.strip()
        if not clean_line:
            continue
        else:
            lines_data.append([float(x) for x in clean_line.split()])

# Teraz tworzymy macierz tylko z poprawnych wierszy z danymi (8 kolumn)
data = np.array(lines_data)
times     = data[:,0]
distances = data[:,1]
endTime   = times[-1]

TExp = 7.7519 * 3600

timesOfMin    = [times[0]]
minDistances  = [distances[0]]
t = 0.0

while (t + TExp < endTime):
    tUp = min(t + 1.5*TExp, endTime)
    start_index = int(np.argmax(times > t + TExp/2))
    end_index   = int(np.argmax(times >= tUp))
    if end_index <= start_index: break

    seg = distances[start_index:end_index]
    minIdx = int(np.argmin(seg))
    minDistance = float(seg[minIdx])
    timeOfMin   = float(times[start_index + minIdx])

    timesOfMin.append(timeOfMin)
    minDistances.append(minDistance)
    t = timeOfMin

timeDiffs = [timesOfMin[i+1] - timesOfMin[i] for i in range(len(timesOfMin)-1)]
savingTimeInterval = times[1] - times[0]

with open(outputDir+fileName,'w') as f_out:
    f_out.write(str(header)+"\n")
    f_out.write(f"Różnica czasu zapisywanych kroków: {savingTimeInterval}\n")
    for x in timeDiffs:
        f_out.write(f"{x:.10f}\n")

'''
if len(timeDiffs) > 0:
    plt.figure(figsize=(8, 5))
    orbity = range(1, len(timeDiffs) + 1)
    plt.scatter(orbity, timeDiffs, label='Zmierzony okres orbitalny')
    plt.axhline(y=timeDiffs[0], color='k', linestyle='--', alpha=0.5, label='Okres referencyjny')
    plt.xlabel('Numer orbity')
    plt.ylabel('Okres orbitalny [s]')
    plt.title('Skracanie okresu orbitalnego wskutek emisji fal grawitacyjnych')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.ylim(timeDiffs[0]-0.5*savingTimeInterval,timeDiffs[0]+0.5*savingTimeInterval)
    plt.savefig(os.path.join(outputDir, "wykres_getMins_okresy.pdf"), bbox_inches='tight')
    plt.close()
    print("[SUKCES] Wygenerowano wykres: wykres_getMins_okresy.pdf")
'''