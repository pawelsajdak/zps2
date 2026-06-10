#ifndef SIMULATION_H
#define SIMULATION_H

#include "Vector.h"

class Simulation{

    double m, mu, eta;
    Vector X, V;
    double tStep;
    bool to2PN;

    const double G = 1.327 * 1.e11;     // km^3/Mo/s^2
    const double c = 3.e5;      // km/s

    // Calculates acceleration for given position and velocity vectors
    Vector calcAcc (const Vector& pos, const Vector& vel);

    public:
    Simulation(
        double tStep_ = 1.0, bool to2PN_ = false, double m1 = 1.387, double m2 = 1.441, 
        double r0 = 746600.0, double v0x = 0.0, double v0y = 900.0)
    {
        tStep = tStep_;
        to2PN = to2PN_;
        m = m1+m2;
        mu = m1*m2/m;
        eta = mu/m;
        X = Vector(r0, 0.);
        V = Vector(v0x, v0y);
    }

    void Print();
    void PrintMag();

    // Goes one step forward
    void Proceed();

};

#endif