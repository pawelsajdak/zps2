#include <iostream>
#include <iomanip>
#include "stdlib.h"
#include "Simulation.h"

int main(int argc, char* argv[]){    
    if (argc < 3){
        std::cout << "Podaj krok czasowy i calkowity czas" << std::endl;
        return 1;
    }

    bool to2PN = true;

    double tStep = atof(argv[1]);
    double totalTime = atof(argv[2]);
    std::cout << "Krok czasowy \t Calkowity czas \t Liczba krokow \t to2PN?" << std::endl;

    long int nSteps = totalTime / tStep;
    std::cout << tStep << "\t" << totalTime << "\t" << nSteps << "\t" << to2PN << std::endl << "Ekstrema lokalne:" << std::endl;
    std::cout << "Czas \t Odleglosc" << std::endl << std::setprecision(15);

    // Symulacja
    Simulation sim(tStep, to2PN);
    double lastDistance = sim.GetMagX();
    bool distanceIsGrowing = true;

    for (long int i=0; i<nSteps; i++)
    {
        double currentDistance = sim.GetMagX();
        if(distanceIsGrowing){
            if(currentDistance < lastDistance)
            {
                std::cout << i*tStep << "\t" << 0.5*(lastDistance+currentDistance) << std::endl;
                distanceIsGrowing = false;
            }
        }
        else{
            if(currentDistance > lastDistance)
            {
                std::cout << -i*tStep << "\t" << 0.5*(lastDistance+currentDistance) << std::endl;
                distanceIsGrowing = true;
            }
        }

        lastDistance = currentDistance;
        sim.Proceed();
    }

    return 0;
}