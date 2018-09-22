#ifndef _PID_H_
#define _PID_H_
class PIDImpl;
class PID
{
public:
        PID(double dt,double max,double min,double Kp,double Kd,double Ki);
        double calculate(double setpoint,double pv);
        ~PID();
private:
    PIDImpl*pimpl;

};
#endif // _PID_H
