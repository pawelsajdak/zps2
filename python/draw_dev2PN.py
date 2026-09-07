#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import os

# Skrypt do stworzenia wykresu ze średnią kwadratową odchyleń dla różnych kroków czasowych (2PN)

x = ["1","0.1","0.01"]
y = [0.02322719, 0.00023978, 0.00001367]

plt.scatter(x,y)
plt.xlabel("Krok czasowy [s]")
plt.ylabel("Średnia kwadratowa odchylenia [km]")
plt.title("Odchylenie kolejnych odległości w periastronie\n od początkowej wartości\n przy poprawkach do rzędu 2PN")

plt.savefig("wyborKrokuCzasowego.pdf", format='pdf', bbox_inches='tight')
plt.close()