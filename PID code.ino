int analogPin = 3;     // connected to pressure sensors (middle terminal) connected to analog pin 3

int Kp ;//constant multiplied with the Proportional to fine tune the system
int Ki ;//constant multiplied with the integral part to fine tune the system 
int Kd ;//constant multiplied with the differential part to fine tune the system                       
int val = 0;           // variable to store the value read
int p ;
int i ;
int d ;
int e ;
int s ;
int t1;
int t2=1;

void set (int sp,int p,int i,int d)
{
  s=sp;
  Kp=p;
  Ki=i;
  Kd=d;
}


void setup()
{
  Serial.begin(9600);              //  setup serial(9600 times the arduino chip will commuicaten with the computer
}

void loop()
{
  t1++;
  val = analogRead(analogPin);     // read the input pin
  Serial.println(val);             // debug value
  e = s-val; 
p=e*Kp;
i=(i+e)*Ki;
d=((e-d)/(t2-t1))*Kd;
t2++;
}
