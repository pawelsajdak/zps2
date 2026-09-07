#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import os

# Skrypt do stworzenia wykresu ze średnią kwadratową odchyleń dla różnych kroków czasowych (2PN)

x = ["1","0.1","0.01","0.001"]
y = [2.31721e-02, 2.30481e-04, 2.53821e-06, 6.52508e-06]

plt.scatter(x,y)
plt.xlabel("Krok czasowy [s]")
plt.ylabel("Średnia kwadratowa odchylenia [km]")
plt.yscale('log')
plt.title("Odchylenie kolejnych odległości w periastronie\n od początkowej wartości\n przy poprawkach do rzędu 2PN")

plt.savefig("krokCzasowy_e7.pdf", format='pdf', bbox_inches='tight')
plt.close()