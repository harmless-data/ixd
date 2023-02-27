// Include the AccelStepper Library
#include <AccelStepper.h>
#include <ezButton.h>

// Define pin connections
const int dirPin = 4;
const int stepPin = 3;

// Define motor interface type
#define motorInterfaceType 1

// Creates an instance
AccelStepper myStepper(motorInterfaceType, stepPin, dirPin);

ezButton forwardLimit(A0);
ezButton backwardLimit(A1);

enum ExecMode {
  ready,
  move,
  home,
};

enum HomeMode{
  forward,
  backward,
};

ExecMode currentExecMode;
HomeMode currentHomeMode;

bool forwardLimitSet = false;
bool backwardLimitSet = false;

long moveToPos = 0;
int moveDir = 1;

int homeSpeed = 900;
int moveSpeed = 300;

int MINPOS = 0;
int MAXPOS = 0;

int signal = NULL;

void setup() {

  currentExecMode = home;
  currentHomeMode = forward;

  forwardLimit.setDebounceTime(50);
  backwardLimit.setDebounceTime(50);

  myStepper.setMaxSpeed(1000);
  myStepper.setSpeed(homeSpeed);
  Serial.begin(9600);
  Serial.println("startup complete\n");

}

void __loop(){
  // Serial.print(".");
  //Serial.println(digitalRead(A1));
  // Serial.println(digitalRead(A0));

  forwardLimit.loop();
  backwardLimit.loop();

  if (backwardLimit.isPressed()){
    Serial.println("back");
  }

  if (forwardLimit.isPressed()){
    Serial.println("forward");
  }

}

void loop() {
  // loop for limit Switches
  forwardLimit.loop();
  backwardLimit.loop();

  if (backwardLimit.isPressed()){
    Serial.println("back");
  }

  if (forwardLimit.isPressed()){
    Serial.println("forward");
  }

  // Serial.println(myStepper.currentPosition()); 

  switch (currentExecMode){
    case home:
      if (forwardLimitSet & backwardLimitSet){
        // Serial.println(F("Homed and Ready"));
        setMoveToPercent(50);
        return;
      }
      myStepper.runSpeed();

      switch(currentHomeMode){
        case forward:
          myStepper.setSpeed(homeSpeed);
          // Serial.println("looking for forward limit");
            if (forwardLimit.isPressed()){
              Serial.println(F("Set Forward Limit"));
              forwardLimitSet = true; 
              MAXPOS = myStepper.currentPosition();
              currentHomeMode = backward;
              return;
            } else {
              return;
            }
        case backward:
          myStepper.setSpeed(-1 * homeSpeed);
          // Serial.println("looking for backward limit");

            if (backwardLimit.isPressed()){
              Serial.println(F("Set Backward Limit"));
              backwardLimitSet = true;
              MINPOS = myStepper.currentPosition();
              myStepper.setSpeed(100);
              currentHomeMode = forward;
              return;
            } else {
              return;
            }
      };
    
      case move:

        myStepper.setSpeed(moveSpeed * moveDir);

        if (forwardLimit.isPressed()){
          // Serial.println("forward bounce");
          myStepper.stop();
          myStepper.setSpeed(0);
          setMoveToPercent(10);
          return;
        }

        if (backwardLimit.isPressed()){
          // Serial.println("backward bounce");
          myStepper.stop();
          myStepper.setSpeed(0);
          setMoveToPercent(90);
          return;
        }

        if(myStepper.distanceToGo() == 0){
          currentExecMode = ready;
        } else { 
          myStepper.run();
        } 
        return;
      
      case ready:
        myStepper.setSpeed(0);
        signal = Serial.parseInt();

        if (signal != NULL){
          setMoveToPercent(signal);
        }
  };
}


void setMoveToPercent(int posPercent){
  //Serial.print(F("Setting MoveTo "));

  int _posPercent = posPercent;

  moveToPos = MINPOS + (abs(MAXPOS - MINPOS)/100)*abs(_posPercent%100);

  moveDir = moveToPos < myStepper.currentPosition() ? -1 : 1;
  Serial.print(moveToPos);
  myStepper.moveTo(moveToPos);
  currentExecMode = move;
}

void _park(){
  return;
}
