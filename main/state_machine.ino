// MODES:
// -1 : Un-Initialized
//  0 : Receive USB Commands
//  1 : Knob Control

int MODE = -1;
String DISPLAY_MESSAGE = "";

void StateSetup() {
  SetState(0);
}

void StateLoop() {
  ButtonCheck();

  if(MODE == 0){
    UsbLoop();
    ServoLoop();
  } else if(MODE == 1){
    KnobLoop();
    ServoLoop();
  }

  
  ClearScreen();
  display.print(DISPLAY_MESSAGE);
  String OUT_MSG = "\n" + String(CURRENT_VALS[0]) + " " + String(CURRENT_VALS[1]) + " " + String(CURRENT_VALS[2]);
  display.print(OUT_MSG);
  display.display();
  delay(20);
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
    DISPLAY_MESSAGE += "  USB\n";
  } else if(state_mode == 1){
    DISPLAY_MESSAGE += "  Knobs\n";
  }

  ClearScreen();
  display.print("LOADING...");
  display.display();
  delay(1000);
}
