#ifndef SIMULATION_H
#define SIMULATION_H

#include "Vector.h"

class Simulation{

    double m, mu, eta;  // masa układu, masa zredukowana, eta
    Vector X, V;        // położenie, prędkość
    double tStep;       // krok czasowy
    bool to2PN;         // symulacja tylko do poprawek rzędu 2PN

    // Stałe fizyczne
    const double G = 1.327 * 1.e11; // km^3/M_o/s^2
    const double c = 3.e5;          // km/s

    // Wyznaczenie wektora przyspieszenia dla danego położenia i prędkości
    // "calculate acceleration"
    Vector calcAcc (const Vector& pos, const Vector& vel);

    public:
        Simulation(
            double tStep_ = 1.0, bool to2PN_ = false, 
            double m1 = 1.4414, double m2 = 1.3867, 
            double r0 = 746600.0,   // początkowa odległość minimalna w periastronie
            double v0x = 0.0, double v0y = 901.6    // początkowe składowe prędkości
        )
        {
            tStep = tStep_;
            to2PN = to2PN_;
            m = m1+m2;
            mu = m1*m2/m;
            eta = mu/m;
            X = Vector(r0, 0.);
            V = Vector(v0x, v0y);
        }

        void Print() const;
        void PrintMag() const;
        double GetMagX() const  { return X.Mag(); }
        double GetMagV() const  { return V.Mag(); }
        
        // Wykonanie jednego kroku do przodu
        void Proceed();

};

#endif