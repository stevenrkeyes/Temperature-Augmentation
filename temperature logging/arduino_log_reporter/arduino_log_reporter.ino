/*************************************************** 
Get the Adafruit_MLX90614 library here
https://github.com/adafruit/Adafruit-MLX90614-Library/archive/master.zip
 ****************************************************/

#include <Wire.h>
#include <Adafruit_MLX90614.h>

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void setup() {
  Serial.begin(9600);

  //Serial.println("Adafruit MLX90614 test");  

  mlx.begin();  
}

void loop() {
  
  if (Serial.available()) {
    // kill the incoming byte
    Serial.read();
    
    // send the data
    Serial.print(mlx.readAmbientTempC()); 
    Serial.print(","); 
    Serial.print(mlx.readObjectTempC());
  }
}
