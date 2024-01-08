
const int BUTTON_PIN = 4;

void ButtonSetup() {
  pinMode(BUTTON_PIN, INPUT);
}

int GetButtonState(){
  if (digitalRead(BUTTON_PIN) == LOW) {
      return 0;
  }

  return 1;
}