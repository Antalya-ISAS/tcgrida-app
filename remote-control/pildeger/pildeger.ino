#include <Adafruit_Sensor.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>
#define SCREEN_WIDTH 128 // OLED display width, in pixels if 96 replace with 96.
#define SCREEN_HEIGHT 64 // OLED display height, in pixels if 32 replace with 32.
#define OLED_RESET     20 // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
void setup() {
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // initialize I2C addr to 0x3C ( for 128x64 Display )
  display.clearDisplay();
  display.display();
  display.setTextSize(1);
  display.setTextColor(BLACK,WHITE);
  display.clearDisplay();


}

void loop() {
  
  display.setCursor(105,1);
  display.print("%20");
  display.drawRect(104,0,19,9,WHITE);
  display.drawLine(123,1,123,7,WHITE);
  display.drawLine(124,3,124,5,WHITE);
  display.display();
}
