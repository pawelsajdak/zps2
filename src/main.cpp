/*
  * Copyright (c) 2026 Paweł Sajdak, Franciszek Drągowski
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
  *
  * This program is distributed in the hope that it will be useful,
  * but WITHOUT ANY WARRANTY; without even the implied warranty of
  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  * GNU General Public License for more details.
  *
  * You should have received a copy of the GNU General Public License
  * along with this program. If not, see <https://www.gnu.org/licenses/>.
*/
///////////////////////////////////////////////


// Program przeprowadza symulację wykorzystującą algorytm Rungego-Kutty 4. rzędu
// Do pliku wyjściowego wypisywane są czasy i separacje (r) dla minimów i ekstremów r
// Czas wystąpienia minimum r zapisywany jest jako liczba ujemna
// Symulacja jest domyślnie przeprowadzana uwzględniając poprawki do rzędu 2,5PN
// Podanie "to2PN = true" powoduje nieuwzględnianie rzędu 2,5PN (poprawki stają się uwzględniane tylko do rzędu 2PN)

// Wywołanie:
// main <całkowity czas> <krok czasowy> [to2PN]


#include <iostream>
#include <iomanip>
#include "stdlib.h"
#include "Simulation.h"


int main(int argc, char* argv[]){    
    if (argc < 3){
        std::cerr << "Podaj calkowity czas oraz krok czasowy" << std::endl;
        return 1;
    }

    // Wczytanie parametrów
    double totalTime = atof(argv[1]);
    double tStep = atof(argv[2]);

    bool to2PN = false;
    if (argc > 3)   to2PN = atoi(argv[3]);

    // Wypisanie parametrów
    std::cout << "Calkowity czas \t Krok czasowy \t Liczba krokow \t to2PN?" << std::endl;

    long int nSteps = totalTime / tStep;
    std::cout << totalTime << "\t" << tStep << "\t" << nSteps << "\t" << to2PN << std::endl;
    std::cout << "t \t r" << std::endl;
    std::cout << std::scientific << std::setprecision(10);


    ///////////////// Symulacja ///////////////////////
    Simulation sim(tStep, to2PN);
    double lastDistance = sim.GetMagX();
    bool distanceIsGrowing = true;

    for (long int i=0; i<nSteps; i++)
    {
        double currentDistance = sim.GetMagX();
        if(distanceIsGrowing){
            if(currentDistance < lastDistance)
            {
                std::cout << (i-1)*tStep << "\t" << lastDistance << std::endl;
                distanceIsGrowing = false;
            }
        }
        else{
            if(currentDistance > lastDistance)
            {
                std::cout << -(i-1)*tStep << "\t" << lastDistance << std::endl;
                distanceIsGrowing = true;
            }
        }

        lastDistance = currentDistance;
        sim.Proceed();
    }

    return 0;
}