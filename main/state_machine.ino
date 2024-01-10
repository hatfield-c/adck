
// MODES:
// -1 : Un-Initialized
//  0 : Potentiometer Control
//  1 : Receive USB Commands
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
    UsbLoop();
    ServoLoop();
  }
}

void ButtonCheck(){
  int button_state = GetButtonState();

  if(button_state == 0){
    int next_mode = MODE + 1;

    if(next_mode > 1){
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
