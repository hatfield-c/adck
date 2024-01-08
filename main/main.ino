
void setup() {
  
  ButtonSetup();
  ServoSetup();
  DisplaySetup();
  StateSetup();
  UsbSetup();

  delay(50);
}

void loop() {
  StateLoop();
  delay(50);
}
