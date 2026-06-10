#include "Simulation.h"
#include <iostream>


Vector Simulation::calcAcc (const Vector& pos, const Vector& vel){
    double r = pos.Mag();
    Vector n = pos*(1/r);
    double v = vel.Mag();
    double rDot = vel*n;

    double A1 = -(1+3*eta)*v*v  +   (3/2)*eta*rDot*rDot +   2*(2+eta)*(m/r) *G;
    A1 /= c*c;
    double A2 = -eta*(3-4*eta)*v*v*v*v + 0.5*eta*(13-4*eta)*v*v*(m/r)*G;
    A2 +=       (3/2)*eta*(3-4*eta)*v*v*rDot*rDot + (2+25*eta+2*eta*eta)*rDot*rDot*(m/r)*G;
    A2 +=       -(15/8)*eta*(1-3*eta)*rDot*rDot*rDot*rDot - (3/4)*(12+29*eta)*(m/r)*(m/r)*G*G;
    A2 /= c*c*c*c;

    double B1 = 2*(2-eta);
    B1 /= c*c;
    double B2 = 0.5*eta*(15+4*eta)*v*v - (3/2)*eta*(3+2*eta)*rDot*rDot;
    B2 +=       -0.5*(4+41*eta+8*eta*eta)*(m/r)*G;
    B2 /= c*c*c*c;

    double A25, B25;

    if(to2PN){
        A25 = 0.0;
        B25 = 0.0;
    }
    else{   // A(and B)_{2.5 PN}
        A25 = 3*v*v + (17/3)*(m/r)*G;
        A25 *= G;
        A25 /= c*c*c*c*c;
        B25 = v*v + 3*(m/r)*G;
        B25 *= G;
        B25 /= c*c*c*c*c;
    }

    // Coefficient at the vector n
    double nCoeff = -1 + A1+A2 + (8/5)*eta*(m/r)*rDot*A25;
    nCoeff *= G*(m/(r*r));

    // Coefficient at the vector v
    double vCoeff = rDot*(B1+B2) - (8/5)*eta*(m/r)*B25;
    vCoeff *= G*(m/(r*r));

    // Building the acceleration vector
    Vector Acc = n*nCoeff + vel*vCoeff;

    return Acc;
}

void Simulation::Proceed() {
    
    Vector k1 = calcAcc (X, V);

    Vector X2 = X + 0.5*tStep*V;
    Vector V2 = V + 0.5*tStep*k1;
    Vector k2 = calcAcc (X2, V2);
    
    Vector X3 = X + 0.5*tStep*V2;
    Vector V3 = V + 0.5*tStep*k2;
    Vector k3 = calcAcc (X3, V3);

    Vector X4 = X + tStep*V3;
    Vector V4 = V + tStep*k3;
    Vector k4 = calcAcc (X4, V4);

    X += (tStep/6)*(V + 2*V2 + 2*V3 + V4);
    V += (tStep/6)*(k1 + 2*k2 + 2*k3 + k4);
}

void Simulation::Print(){
    X.Print();
    V.Print();
}

void Simulation::PrintMag(){
    std::cout << X.Mag() << "\t" << V.Mag();
}