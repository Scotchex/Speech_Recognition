#include <Arduino.h>
char userInput;

void setup(){
  pinMode(3, OUTPUT);
  Serial.begin(9600);                        

}

void loop(){

while(Serial.available()> 0){ 
    
    userInput = Serial.read();             
      
      if(userInput == '1'){                  
        digitalWrite(3, HIGH);
        
      }
       else {
          digitalWrite(3, LOW);
        }

       
                        
            
      
      } 
  }
