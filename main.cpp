#include <Arduino.h>
int led_DIGITAL_PIN = 3;
void setup() {
  Serial.begin(9600);
  
  pinMode(led_DIGITAL_PIN, OUTPUT);
}
int value=0;


 
void loop() 
   {
     while (Serial.available())
        {
           value = Serial.read();
        }
     Serial.print(value);
     if (value == 1)
        digitalWrite (led_DIGITAL_PIN, HIGH);
     
     else if (value == 2)
        digitalWrite (led_DIGITAL_PIN, LOW);
   }