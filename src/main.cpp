#include <iostream>
#include "stdlib.h"
#include "Simulation.h"

int main(int argc, char* argv[]){    
    if (argc < 3){
        std::cout << "Podaj krok czasowy i calkowity czas" << std::endl;
        return 1;
    }

    double tStep = atof(argv[1]);
    double totalTime = atof(argv[2]);

    long int nSteps = totalTime / tStep;
    std::cout << "Liczba krokow: " << nSteps << std::endl;

    bool to2PN = true;
    Simulation sim(tStep, to2PN);

    for (long int i=0; i<nSteps; i++)
    {
        sim.Proceed();

        if(i%1 == 0)
        {
            std::cout << i*tStep << "\t";
            sim.PrintMag();
            std::cout << "\n";
        }
    }

    return 0;
}