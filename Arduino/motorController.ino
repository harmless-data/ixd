// Include the AccelStepper Library
#include <AccelStepper.h>

// Define pin connections
const int dirPin = 4;
const int stepPin = 3;




// Define motor interface type
#define motorInterfaceType 1


// Creates an instance
AccelStepper myStepper(motorInterfaceType, stepPin, dirPin);

void setup() {


  myStepper.setMaxSpeed(150);
  myStepper.setAcceleration(100);

}

void loop() {

myStepper.moveTo(500);
  myStepper.setSpeed(100);
  myStepper.runSpeedToPosition();

  delay(6000);
  

}
