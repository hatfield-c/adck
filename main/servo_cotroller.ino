#include <Servo.h>

Servo SERVOS[3];
float OFFSETS[3];
int CURRENT_VALS[3];
int DESIRED_VALS[3];
int INIT_VALS[3] = { 90, 90, 90 };
int MAX_SERVO_DIFF = 5;

void SetServo(int index, int value){
  DESIRED_VALS[index] = value;
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
    if(CURRENT_VALS[i] != DESIRED_VALS[i]){
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
    int servo_value = DESIRED_VALS[i];
    int current_value = CURRENT_VALS[i];

    int servo_diff = servo_value - current_value;
    int direction_sign = servo_diff / abs(servo_diff);

    if(abs(servo_diff) > MAX_SERVO_DIFF){
      servo_value = current_value + (direction_sign * MAX_SERVO_DIFF);
    }

    CURRENT_VALS[i] = servo_value;

    WriteServo(i, servo_value + servo_offset);
  }
}