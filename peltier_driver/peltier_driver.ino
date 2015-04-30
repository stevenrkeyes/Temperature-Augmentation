const int peltier_hot_pin = 9;
const int peltier_cold_pin = 10;

void setup() {
  // initialize serial communications at 9600 bps for reporting to computer
  Serial.begin(9600); 
}

void loop() {
  // i wouldn't go above PWM 192 or so,
  // otherwise the H bridge really starts to heat up
  
  // heat up the labeled side
  analogWrite(peltier_hot_pin, 192);
  analogWrite(peltier_cold_pin, 0);
  delay(5000);
  
  // cool the labeled side
  analogWrite(peltier_hot_pin, 0);
  analogWrite(peltier_cold_pin, 192);
  delay(5000);
}
