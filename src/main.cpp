#include <iostream>
#include "Simulation.h"

int main(){
    
    Simulation sim(1.e-3);

    for (int i=0; i<3.e7; i++)
    {
        sim.Proceed();

        if(i%10000 == 0)
        {
            std::cout << "Step " << i << std::endl;
            sim.Print();
            std::cout << "\n";
        }
    }

    return 0;
}