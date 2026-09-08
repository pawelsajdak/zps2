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

#include "Simulation.h"
#include <iostream>


Vector Simulation::calcAcc (const Vector& pos, const Vector& vel){
    double r = pos.Mag();   // odległość
    Vector n = pos*(1/r);   // wersor n
    double v = vel.Mag();   // wartość prędkości
    double rDot = vel*n;    // dr/dt = prędkość * n (iloczyn skalarny)

    // Obliczenie współczynników do poprawek post-newtonowskich

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

    // poprawki 2.5PN
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


    // Konstruowanie wektora przyspieszenia

    // współczynnik przy wersorze n
    double nCoeff = -1 + A1+A2 + (8/5)*eta*(m/r)*rDot*A25;
    nCoeff *= G*(m/(r*r));

    // współczynnik przy wektorze v
    double vCoeff = rDot*(B1+B2) - (8/5)*eta*(m/r)*B25;
    vCoeff *= G*(m/(r*r));

    // wektor przyspieszenia
    Vector Acc = n*nCoeff + vel*vCoeff;

    return Acc;
}


void Simulation::Proceed() {    
    // Zmiana wektorów X i V zgodnie z algorytmem RK4
    
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

void Simulation::Print() const{
    X.Print();
    V.Print();
}

void Simulation::PrintMag() const{
    std::cout << X.Mag() << "\t" << V.Mag();
}