#include <Adafruit_Sensor.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>

#include <Wire.h>


#include <SPI.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels
#define OLED_RESET     20 // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
#define IUDSZ_BMPWIDTH  128
#define IUDSZ_BMPHEIGHT  60
void setup() {
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // initialize I2C addr to 0x3C ( for 128x64 Display )
  display.clearDisplay();
  display.display();
  display.setTextSize(2); 
  display.setTextColor(WHITE);
  display.clearDisplay();
}

void loop() {
  // put your main code here, to run repeatedly:
    display.setCursor(0,0);
    display.print("   Bilgi");
    display.setCursor(22,16);
    display.print("x1:");
    display.setCursor(58,16);
    display.print("1500");
    display.setCursor(22,32);
    display.print("x2:");
    display.setCursor(58,32);
    display.print(3000 - (1500)); 
    display.setCursor(22,48);
    display.print("y2:");
    display.setCursor(58,48);
    display.print("1500");
     display.display();
}
