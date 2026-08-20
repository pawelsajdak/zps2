#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

dataFile = "../build/out.txt"
data = np.loadtxt(dataFile, skiprows=3)
N = data.shape[0]

# Rysuj co n-ty punkt
n = 4
slimmedData = data[::n,:]

plt.scatter(slimmedData[:,0],slimmedData[:,1],s=1)
plt.xlabel("Czas")
plt.ylabel("Odleglosc")
plt.savefig("plot.pdf")