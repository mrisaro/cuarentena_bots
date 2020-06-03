#include <Adafruit_Sensor.h>
#include "Adafruit_BMP280.h"

Adafruit_BMP280 bmp; // I2C
//Variable para guardar los valores recibidos desde Python
unsigned int dato;

float presion; // Almacena la presion atmosferica (Pa)
float temperatura; // Almacena la temperatura (oC)
int altitud; // Almacena la altitud (m) (se puede usar variable float)


void setup() {

 bmp.begin(); // Inicia el sensor
 Serial.begin(9600); // Inicia comunicacion serie
}

void loop() {
  if(Serial.available()>0){
    // read serial port
    dato=Serial.read();
    
    if(dato=='P'){
      presion = bmp.readPressure()/100;
      temperatura = bmp.readTemperature();
      Serial.println(presion);
    }
  delay(1000);
  }
}
