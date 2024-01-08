
void setup() {
  
  ButtonSetup();
  PotentiometerSetup();
  DisplaySetup();
  StateSetup();

  delay(3000);
}

void loop() {
  StateLoop();
  delay(50);
}
