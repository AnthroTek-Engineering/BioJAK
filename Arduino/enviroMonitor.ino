//Arduino 1.0+ Only!
//Arduino 1.0+ Only!

#include <Wire.h>
#include <ADXL345.h>
#include "DHT.h"
#include <String.h>

#define DHT1PIN 5     
#define DHT2PIN 6

#define DHT1TYPE DHT22  
#define DHT2TYPE DHT22  

DHT dht1(DHT1PIN, DHT1TYPE);
DHT dht2(DHT2PIN, DHT2TYPE);

String data;

int im = 0;
int f  = 0;
int in = 0;



ADXL345 adxl; //variable adxl is an instance of the ADXL345 library

void setup(){
  Serial.begin(9600);
  adxl.powerOn();

  dht1.begin();
  dht2.begin();
  
  
  //set activity/ inactivity thresholds (0-255)
  adxl.setActivityThreshold(70); //62.5mg per increment
  adxl.setInactivityThreshold(70); //62.5mg per increment
  adxl.setTimeInactivity(1); // how many seconds of no activity is inactive?
  
  adxl.setActivityX(1);
  adxl.setActivityY(1);
  adxl.setActivityZ(1);
  
  //look of inactivity movement on this axes - 1 == on; 0 == off
  adxl.setInactivityX(1);
  adxl.setInactivityY(1);
  adxl.setInactivityZ(1);

  //look of tap movement on this axes - 1 == on; 0 == off
  adxl.setTapDetectionOnX(1);
  adxl.setTapDetectionOnY(1);
  adxl.setTapDetectionOnZ(1);

  //set values for what is a tap, and what is a double tap (0-255)
  adxl.setTapThreshold(255); //62.5mg per increment
  adxl.setTapDuration(2); //625μs per increment
  adxl.setDoubleTapLatency(80); //1.25ms per increment
  adxl.setDoubleTapWindow(200); //1.25ms per increment

  //set values for what is considered freefall (0-255)
  adxl.setFreeFallThreshold(7); //(5 - 9) recommended - 62.5mg per increment
  adxl.setFreeFallDuration(70); //(20 - 70) recommended - 5ms per increment

  //setting all interupts to take place on int pin 1
  //I had issues with int pin 2, was unable to reset it
  adxl.setInterruptMapping( ADXL345_INT_SINGLE_TAP_BIT,   ADXL345_INT1_PIN );
  adxl.setInterruptMapping( ADXL345_INT_DOUBLE_TAP_BIT,   ADXL345_INT1_PIN );
  adxl.setInterruptMapping( ADXL345_INT_FREE_FALL_BIT,    ADXL345_INT1_PIN );
  adxl.setInterruptMapping( ADXL345_INT_ACTIVITY_BIT,   ADXL345_INT1_PIN );
  adxl.setInterruptMapping( ADXL345_INT_INACTIVITY_BIT,   ADXL345_INT1_PIN );

  //register interupt actions - 1 == on; 0 == off  
  adxl.setInterrupt( ADXL345_INT_SINGLE_TAP_BIT, 1);
  adxl.setInterrupt( ADXL345_INT_DOUBLE_TAP_BIT, 1);
  adxl.setInterrupt( ADXL345_INT_FREE_FALL_BIT,  1);
  adxl.setInterrupt( ADXL345_INT_ACTIVITY_BIT,   1);
  adxl.setInterrupt( ADXL345_INT_INACTIVITY_BIT, 1);
  
}

void loop(){

  String t1 = String((int)dht1.readTemperature());
  String t2 = String((int)dht2.readTemperature());
  
  String h1 = String((int)dht1.readHumidity());
  String h2 = String((int)dht2.readHumidity());

  int x,y,z;  
  adxl.readAccel(&x, &y, &z); 

  byte interrupts = adxl.getInterruptSource();
  
  if(adxl.triggered(interrupts, ADXL345_INACTIVITY)){
     in = in + 1;
  }
  
  if(adxl.triggered(interrupts, ADXL345_ACTIVITY)){
     in = 0;
  }

  // freefall
  if(adxl.triggered(interrupts, ADXL345_FREE_FALL)){
    f = f + 1;
  }

  //double tap
  if(adxl.triggered(interrupts, ADXL345_DOUBLE_TAP)){

  }

  //tap
  if(adxl.triggered(interrupts, ADXL345_SINGLE_TAP)){
    im = im + 1;
  } 
  
  data = t1+","+t2+","+h1+","+h2+","+im+","+f+","+in+","+x+","+y+","+z;
  Serial.println(data);
  
 delay(1000);
}

