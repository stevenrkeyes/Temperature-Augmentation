#include <SoftPWM.h>

const int peltier_out_pin = 13; // output pin to be PWMed

int output_value = 128;        // value output to the PWM (analog out)


void setup() {
  // initialize serial communications at 9600 bps for reporting to computer
  Serial.begin(9600); 
  
  // we need software pwm to pwm pin 13
  SoftPWMBegin();
  SoftPWMSet(peltier_out_pin, 0);
  
}

void loop() {  
  
  // do stuff here to calculate output_value
  
  // 0 <= output_value < 256
  //SoftPWMSet(peltier_out_pin, output_value);
  SoftPWMSet(peltier_out_pin, 0);
  delay(6000);
  SoftPWMSet(peltier_out_pin, 128);
  delay(6000);
  SoftPWMSet(peltier_out_pin, 192);
  delay(6000);
  SoftPWMSet(peltier_out_pin, 255);
  delay(6000);
  SoftPWMSet(peltier_out_pin, 0);
  delay(6000);
  
}
