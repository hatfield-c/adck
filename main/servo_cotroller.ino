#include <Servo.h>

Servo SERVOS[3];
float OFFSETS[3];
int OLD_VALS[3];
int NEW_VALS[3];
int INIT_VALS[3] = { 90, 90, 90 };

void SetServo(int index, int value){
  NEW_VALS[index] = value;
}

void SetServos(int values[]){
  for(int i = 0; i < 3; i++){
    SetServo(i, values[i]);
  }
}

void WriteServo(int index, int value){
  SERVOS[index].write(value);
}

bool IsUpdated(){
  for(int i = 0; i < 3; i++){
    if(OLD_VALS[i] != NEW_VALS[i]){
      return true;
    }
  }

  return false;
}

void ServoSetup(){
  SERVOS[0].attach(9);
  SERVOS[1].attach(6);
  SERVOS[2].attach(5);
  
  SetServos(INIT_VALS);
}

void ServoLoop(){
  if(!IsUpdated()){
    return;
  }

  for(int i = 0; i < 3; i++){
    int servo_offset = OFFSETS[i];
    int servo_value = NEW_VALS[i];
    OLD_VALS[i] = servo_value;

    WriteServo(i, servo_value + servo_offset);
  }
}