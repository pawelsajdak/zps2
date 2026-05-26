#include "Vector.h"
#include <iostream>
#include <cmath>


Vector& Vector::operator+=(const Vector& v){
    this->x += v.x;
    this->y += v.y;

    return *this;
}

Vector Vector::operator+(const Vector& v) const{
    double x_ = x + v.x;
    double y_ = y + v.y;

    return Vector(x_,y_);
}

Vector Vector::operator*(double a) const{
    double x_ = x * a;
    double y_ = y * a;

    return Vector(x_,y_);
}

double Vector::operator*(const Vector& v) const{
    double x_ = x * v.x;
    double y_ = y * v.y;

    return x_+y_;
}

double Vector::Mag() const{
    return std::sqrt(x*x + y*y);
}

void Vector::Print() const{
    std::cout << x << "\t" << y << std::endl;
}