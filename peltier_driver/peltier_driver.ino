// the hot pin is the one that causes the labeled side to heat up
const int peltier_hot_pin = 9;
const int peltier_cold_pin = 10;
const int lm355z_pin = A7;

float temperature_K;
float temperature_F;
int reading;
int output_value;

float desired_temperature_F;
float error;

const float proportional_gain = 3;
// i wouldn't go above PWM 192 or so,
// otherwise the H bridge really starts to heat up
const int peltier_pwm_max = 192;

void setup() {
  // initialize serial communications at 9600 bps for reporting to computer
  Serial.begin(9600); 
}

void loop() {
  
  
  reading = analogRead(lm355z_pin);
  temperature_K = map(reading, 0, 1023, 0, 500.0);
  temperature_F = 1.8*(temperature_K - 273) + 32;
  
  desired_temperature_F = 80;
  
  error = desired_temperature_F - temperature_F;
  if (error > 0) {
    // heat up the labeled side
    output_value = min(proportional_gain*error, peltier_pwm_max);
    analogWrite(peltier_hot_pin, output_value);
    analogWrite(peltier_cold_pin, 0);
    digitalWrite(13, HIGH);
  }
  else {
    // cool the labeled side
    output_value = min(-proportional_gain*error, peltier_pwm_max);
    analogWrite(peltier_hot_pin, 0);
    analogWrite(peltier_cold_pin, output_value);
    digitalWrite(13, LOW);
  }
  delay(500);
}
