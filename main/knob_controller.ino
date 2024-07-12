
int KNOB_LOW = 0;
int KNOB_HIGH = 1023;
int ANGLE_LOW = 0;
int ANGLE_HIGH = 180;

int KNOB_ANGLES[4];

int GetKnobAngle(int index){
  int knob_value = analogRead(index);
  int angle_value = map(
    knob_value, 
    KNOB_LOW, 
    KNOB_HIGH, 
    ANGLE_LOW, 
    ANGLE_HIGH
  );

  return angle_value;
}

void KnobLoop(){
  for(int i = 0; i < 4; i++){
    KNOB_ANGLES[i] = GetKnobAngle(i);
  }

  SetServos(KNOB_ANGLES);
}
