#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

dataFile = "../build/out.txt"
data = np.loadtxt(dataFile, skiprows=3)
plt.plot(data[:,0],data[:,1])
plt.xlabel("Czas")
plt.ylabel("Odleglosc")
plt.savefig("plot.pdf")