#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define OLED_RESET     4
Adafruit_SSD1306 display(128, 64, &Wire, OLED_RESET);

void DisplaySetup() {
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.setTextColor(WHITE);

  ClearScreen();

  display.print("Booting...");
  display.display();

  delay(2000);
}

void ClearScreen(){
  display.clearDisplay();
  display.setTextSize(2);
  display.setCursor(0, 0);
}
