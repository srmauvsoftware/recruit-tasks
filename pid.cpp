#ifndef _PID_SOURCE_
#define _PID_SOURCE_

#include <iostream>
#include <cmath>
#include "pid.h"

using  namespace std;

class PIDImpl
{
public:
    PIDImpl(double dt,double max,double min,double Kp,double Kd,double Ki);
    ~PIDImpl();
    double calculate(double setpoint,double pv);

private:
    double _dt;
    double _max;
    double _min;
    double _Kp;
    double _Kd;
    double _Ki;
    double _pre_error;
    double _integral;
};

PID::PID(double dt,double max,double min,double Kp,double Kd,double Ki)
{
    pimpl=new PIDImpl(dt,max,min,Kp,Kd,Ki);
}

double PID::calculate(double setpoint,double pv)
{
    return pimpl->calculate(setpoint,pv);
}
PID::~PID()
{
    delete pimpl;
}
PIDImpl::PIDImpl(double dt,double max,double min,double Kp,double Kd,double Ki):
    _dt(dt),
    _max(max),
    _min(min),
    _Kp(Kp),
    _Kd(Kd),
    _Ki(Ki),
    _pre_error(0),
    _integral(0)
    {

    }
    double PIDImpl::calculate(double setpoint,double pv)
    {
        double error=setpoint-pv;
        double Pout=_Kp*error;
        _integral+=error*_dt;
        double Iout=_Ki*_integral;
        double derivative=(error-_pre_error)/_dt;
        double Dout=_Kd*derivative;
        double output=Pout+Iout+Dout;

        if(output>_max)
            output=_max;
        else if(output<_min)
            output=_min;
        _pre_error=error;

        return output;
    }
    PIDImpl::~PIDImpl()
    {

    }
    #endif
