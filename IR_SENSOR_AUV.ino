/*
 * rosserial Publisher Example
 * Prints "hello world!"
 */

#include <ros.h>
#include <std_msgs/Float64.h>

float x;
ros::NodeHandle  nh;
void messageCb( const std_msgs::Float64& msg)
{
  x = msg.data;
  if(x>5)
  {
    digitalWrite(13, HIGH-digitalRead(13));
  }
}


std_msgs::Float64 str_msg;
ros::Publisher chatter("chatter", &str_msg);
ros::Subscriber<std_msgs::Float64> sub("chatter", messageCb);
float val = 0;



void setup()
{
  Serial.begin(9600);
  pinMode(A0, OUTPUT);
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.advertise(chatter);
  nh.subscribe(sub);
}

void loop()
{
  val = analogRead(A0);
  str_msg.data = val ;

  if(val>13)
  Serial.println("Out of Rnge");
  delay(100);
  Serial.println(val);
  delay(100);
  chatter.publish( &str_msg );
  nh.spinOnce();
  delay(1000);
}





