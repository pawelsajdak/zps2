#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import os

x = ["1","0.1","0.01","0.001"]
y = [0.024113097804277225, 0.00025181058786348927, 0.0002514415609479116, 0.0002508044174798041]

plt.figure(figsize=(4, 4))
plt.scatter(x,y)
plt.xlabel("Krok czasowy [s]")
plt.ylabel("Średnia kwadratowa odchylenia [km]")
plt.title("Odchylenie kolejnych odległości w periastronie\n od początkowej wartości\n przy poprawkach do rzędu 2PN")

plt.savefig("wyborKrokuCzasowego.pdf", format='pdf', bbox_inches='tight')
plt.close()