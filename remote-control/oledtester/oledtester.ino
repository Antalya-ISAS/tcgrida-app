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
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.clearDisplay();
  display.drawRect(2,17,126,46,WHITE);
  display.drawLine(2,40,126,40,WHITE);
  display.drawLine(48,17,48,62,WHITE);

}

void loop() {
  display.drawRect(2,17,126,46,WHITE);
  display.drawLine(2,40,126,40,WHITE);
  display.drawLine(48,17,48,62,WHITE);

  
  display.setCursor(0,0);
  display.print("Cevre Blg.");
   // Show temperature level (Celcius)
  if (11 < 10)
  { 
    display.setCursor(5, 22);
    display.print("Sic");
    display.setCursor(39, 22);
    display.print(":");
    display.setCursor(53, 22);
    display.print("0");
    display.setCursor(82, 22);
    display.print(dis_sicaklik);
    display.setCursor(96,22);
    display.print("C");
  }
  else
  {
    display.setCursor(5, 22);
    display.print("Sic");
    display.setCursor(39, 22);
    display.print(":");
    display.setCursor(68, 22);
    display.print(dis_sicaklik);
    display.print("C");
  }

  // Show humidity level 
  if (11 < 10)
  {
    display.setCursor(5, 44);
    display.print("Nem");
    display.setCursor(39, 44);
    display.print(":");
    display.setCursor(68, 44);
    display.print("%");
    display.setCursor(82, 44);
    display.print(0);
    display.setCursor(96,44);
    display.print(dis_nem);
  }
  else
  { 
    display.setCursor(5, 44);
    display.print("Nem");
    display.setCursor(39, 44);
    display.print(":");
    display.setCursor(68, 44);
    display.print("%");
    display.setCursor(82, 44);
    display.print(dis_nem);

  }
  display.display();
}
