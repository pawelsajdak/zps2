#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

dataFile = "../build/out3.txt"
data = np.loadtxt(dataFile, skiprows=4)

dataMin = data[data[:,0] < 0]
times = -dataMin[:,0]
distanceDevs = dataMin[:,1] - dataMin[0,1]

plt.plot(times,distanceDevs)
plt.xlabel("Czas")
plt.ylabel("Odchylenie odleglosci minimalnej")
# plt.xlim(0,1.e6)
# plt.ylim(-1.e-5,1.e-5)
# plt.yscale('log')
plt.savefig("plot.pdf")