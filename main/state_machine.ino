
// MODES:
// -1 : Un-Initialized
//  0 : Potentiometer Control
//  1 : Calibration Mode: FORWARD
//  2 : Calibration Mode: LEFT
//  3 : Calibration Mode: BACKWARD
//  4 : Calibration Mode: RIGHT
//  5 : Receive USB Commands
int MODE = -1;
String DISPLAY_MESSAGE = "";

void StateSetup() {
  SetState(0);
}

void StateLoop() {
  ButtonCheck();

  if(MODE == 0){
    KnobLoop();
    ServoLoop();
  } else if(MODE == 1){

  } else if(MODE == 2){

  } else if(MODE == 3){

  } else if(MODE == 4){

  } else if(MODE == 5){
    UsbLoop();
    ServoLoop();
  }
}

void ButtonCheck(){
  int button_state = GetButtonState();

  if(button_state == 0){
    int next_mode = MODE + 1;

    if(next_mode > 5){
      next_mode = 0;
    }

    SetState(next_mode);
  }
}

void SetState(int state_mode){
  MODE = state_mode;

  DISPLAY_MESSAGE = "<Mode>:\n";

  if(state_mode == 0){
    DISPLAY_MESSAGE += "  Knobs";
  } else if(state_mode == 1){
    DISPLAY_MESSAGE += "  Forward";
  } else if(state_mode == 2){
    DISPLAY_MESSAGE += "  Left";
  } else if(state_mode == 3){
    DISPLAY_MESSAGE += "  Backward";
  } else if(state_mode == 4){
    DISPLAY_MESSAGE += "  Right";
  } else if(state_mode == 5){
    DISPLAY_MESSAGE += "  USB";
  }

  ClearScreen();
  
  display.print(DISPLAY_MESSAGE);
  display.display();
  delay(1000);
  display.print("\n\n         >");
  display.display();
  delay(20);
}
