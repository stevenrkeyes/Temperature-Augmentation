// the hot pin is the one that causes the labeled side to heat up
const int peltier_hot_pin = 9;
const int peltier_cold_pin = 10;
const int lm355z_pin = A7;

float temperature_K;
float temperature_F;
int reading;
int output_value;

float desired_temperature_F = 110;
float error;
int deadband = 1;

char byte1;
char byte2;
float new_temperature;

const float proportional_gain = 20;
// i wouldn't go above PWM 192 or so,
// otherwise the H bridge really starts to heat up
const int peltier_pwm_max = 192;

void setup() {
  // initialize serial communications at 9600 bps for reporting to computer
  Serial.begin(9600);
  Serial.print("Power On"); 
}

void loop() {
  
  /*if (Serial.available()){
    byte1 = Serial.read();
    byte2 = Serial.read();
    new_temperature = (byte1-48)*10 + (byte2-48;
    if ((32 < new_temperature) && (new_temperature < 100)){
      desired_temperature_F = new_temperature;
    }
    Serial.println(new_temperature);
  }*/
  
  // turn off the peltier device briefly to get a good reading
  analogWrite(peltier_hot_pin, 0);
  analogWrite(peltier_cold_pin, 0);
  delay(10);
  
  reading = analogRead(lm355z_pin);
  temperature_K = map(reading, 0, 1023, 0, 5000)/10.0;
  temperature_F = 1.8*(temperature_K - 273) + 32;
  temperature_F = 1.7079*temperature_F - 26.6882;

  //desired_temperature_F = 70;
  
  Serial.println(temperature_F);
  
  error = desired_temperature_F - temperature_F;
  if (error > deadband) {
    // heat up the labeled side
    output_value = min(70+proportional_gain*error, peltier_pwm_max);
    analogWrite(peltier_hot_pin, output_value);
    analogWrite(peltier_cold_pin, 0);
    digitalWrite(13, HIGH);
  }
  else if (error < -deadband){
    // cool the labeled side
    //output_value = min(70+-proportional_gain*error, peltier_pwm_max);
    output_value = peltier_pwm_max;
    analogWrite(peltier_hot_pin, 0);
    analogWrite(peltier_cold_pin, output_value);
    digitalWrite(13, LOW);
  } else {
    analogWrite(peltier_hot_pin, 0);
    analogWrite(peltier_cold_pin, 0);
    digitalWrite(13, LOW);
  }
  delay(500);
}
