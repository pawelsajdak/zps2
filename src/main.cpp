#include <iostream>
#include <iomanip>
#include "stdlib.h"
#include "Simulation.h"

// Wywołanie:
// main <całkowity czas> <krok czasowy> [interwał wypisu] [to2PN]

int main(int argc, char* argv[]){    
    if (argc < 3){
        std::cerr << "Podaj calkowity czas oraz krok czasowy" << std::endl;
        return 1;
    }

    // Wczytanie parametrów
    double totalTime = atof(argv[1]);
    double tStep = atof(argv[2]);
    
    int outputInterval = 1;
    if (argc > 3)   outputInterval = atoi(argv[3]);

    bool to2PN = false;
    if (argc > 4)   to2PN = atoi(argv[4]);

    // Wypisanie parametrów
    std::cout << "Calkowity czas \t Krok czasowy \t Liczba krokow \t Interwal wypisu \t to2PN?" << std::endl;

    long int nSteps = totalTime / tStep;
    std::cout << totalTime << "\t" << tStep << "\t" << nSteps << "\t" << outputInterval << "\t" << to2PN << std::endl;
    std::cout << "t \t r \t v" << std::endl;
    std::cout << std::scientific << std::setprecision(10);


    ///////////////// Symulacja ///////////////////////
    Simulation sim(tStep, to2PN);

    for (long int i=0; i<nSteps; i++)
    {
        if(i%outputInterval == 0)    // wypisuj po niektórych krokach
        {
            std::cout << i*tStep << "\t";
            sim.PrintMag();
            std::cout << "\n";
        }

        sim.Proceed();
    }

    return 0;
}