/***********************************************************
File name: AdeeptArmInitializationCode.ino
Description: Power on, the servo rotates 90 to straighten the robotic arm
Website: www.adeept.com
E-mail: support@adeept.com
Author: Tom
Date: 2019/04/26
***********************************************************/
// OLED test.
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define OLED_RESET     4
Adafruit_SSD1306 display(128, 64, &Wire, OLED_RESET);

#include <Servo.h>。
int servopin1 = 9;    //Define servo interface digital interface 9
int servopin2 = 6;    //Define servo interface digital interface 6
int servopin3 = 5;    //Define servo interface digital interface 5

int moveServoData;
Servo servo1;
Servo servo2;
Servo servo3;

const char compile_date[] = __DATE__ " " __TIME__;

void setup() {
  // put your setup code here, to run once:
  pinMode(servopin1,OUTPUT);//Set the servo interface as the output interface
  pinMode(servopin2,OUTPUT);//Set the servo interface as the output interface
  pinMode(servopin3,OUTPUT);//Set the servo interface as the output interface
  Serial.begin(9600);
  Serial.setTimeout(1);

  delay(1000);

  // OLED test.
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.setTextColor(WHITE);//Sets the font display color
  display.clearDisplay();//cls
  //Set the font size
  display.setTextSize(2);
  //Set the display location
  display.setCursor(0, 0);
  //String displayed
  display.println(F("BUILD DATE"));
  display.println(compile_date);
  display.println("RIGHT ARM");
  //Began to show
  display.display();
  delay(3000);
}
void loop()
{
  int x;
  String s;

  display.clearDisplay();
  display.setTextSize(2);
  display.setCursor(0, 0);

  while (!Serial.available());
  s = Serial.readString();
  display.println(s);
  x = atoi(s.c_str());

  display.println(x);
  display.println(x + 1);
  display.display();

  servo1.attach(servopin1);
  servo2.attach(servopin2);
  servo3.attach(servopin3);
  servo1.write(90);
  servo2.write(90);
  servo3.write(90);
  delay(20);
}
