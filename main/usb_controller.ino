
void UsbSetup() {
  Serial.begin(9600);
}

void UsbLoop() {
  int position[3];

  UsbGetPosition(position);

  if(position[0] != -1000){
    SetServos(position);
  }

}

void UsbGetPosition(int position[]){
  String raw_string = UsbReadLine();

  if(raw_string == "NULL"){
    position[0] = -1000;

    return;
  }

  char* theta0 = strtok(raw_string.c_str(), ",");
  char* theta1 = strtok(NULL, ",");
  char* theta2 = strtok(NULL, ",");

  position[0] = atoi(theta0);
  position[1] = atoi(theta1);
  position[2] = atoi(theta2);
}

String UsbReadLine() {
  String line = "NULL";

  if(Serial.available()){
    while(Serial.available()){
      line = Serial.readStringUntil('\0');
    }
  }

  return line;
}