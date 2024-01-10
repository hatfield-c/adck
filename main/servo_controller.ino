#include <Servo.h>

Servo SERVOS[3];
float OFFSETS[3] = { 0, 0, 0};
int CURRENT_VALS[3] = { 80, 80, 80 };
int DESIRED_VALS[3] = { 90, 90, 90 };
int INIT_VALS[3] = { 90, 90, 90 };
int MAX_SERVO_DIFF = 8;

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

void ServoSetup(){
  SERVOS[0].attach(9);
  SERVOS[1].attach(6);
  SERVOS[2].attach(5);
  
  SetServos(INIT_VALS);
}

void ServoLoop(){
  
  for(int i = 0; i < 3; i++){
    int servo_offset = OFFSETS[i];
    int servo_value = DESIRED_VALS[i];
    int current_value = CURRENT_VALS[i];

    int servo_diff = servo_value - current_value;
    servo_diff = constrain(servo_diff, -MAX_SERVO_DIFF, MAX_SERVO_DIFF);

    if(servo_diff == 0){
      continue;
    }

    servo_value = current_value + servo_diff;
    CURRENT_VALS[i] = servo_value;  

    WriteServo(i, servo_value + servo_offset);
    delay(10);
  }
}