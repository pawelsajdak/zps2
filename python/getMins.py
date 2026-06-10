#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

dataFile = "../build/out.txt"
data = np.loadtxt(dataFile, skiprows=1)

times = data[:,0]
distances = data[:,1]
tStep = times[1] - times[0]
endTime = times[-1]

TExp = 7.75*3600    # expected orbital period
t = 0

timesOfMin = []
minDistances = []

while (t+TExp/2 < endTime):
    tUp = min([t+1.5*TExp, endTime])
    
