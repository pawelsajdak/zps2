#include <iostream>
#include <iomanip>
#include "stdlib.h"
#include "Simulation.h"

// Wywołanie:
// main <całkowity czas> <krok czasowy> [to2PN]

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