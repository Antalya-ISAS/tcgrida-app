#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
#include <can.h>
#include <mcp2515.h>
#include <Servo.h>
#include <SPI.h>

#define maxdeger 1940 //max 2000 oluyor escler 1000-2000 arası calisir
#define mindeger 1060
#define sabitleme_toleransi 30

struct can_frame canSend;
struct can_frame canRcv;

//CANBUS
MCP2515 mcp2515(8);

float hizBoleni = 1.0;
int button = 2;
bool button_deger = false;
bool clear_state = true;

//LCD için değerler
int dis_sicaklik;
int dis_nem;
int basinc_deger;
int sicak_deger;
bool lcd_durum = false;

//Joystick değerleri - 2 koordinat
int pinJoyStick_X_1 = 1;
int pinJoyStick_Y_1 = 0;
int pinJoyStick_X_2 = 2;
int pinJoyStick_Y_2 = 3;

int valueJoyStick_X_1 = 0;
int valueJoyStick_Y_1 = 0;
int valueJoyStick_X_2 = 0;
int valueJoyStick_Y_2 = 0;

union ArrayToInteger {
  byte array[2];
  int integer;
} converter;
union ArrayToDouble {
  byte array[4];
  double number;
} doubler;


void setup()
{
  Serial.begin(9600);
  SPI.begin();
  
  lcd.begin();
  lcd.home();
  lcd.print("TCG Grida");
  delay(5000);
  
  pinMode(button , INPUT);
  attachInterrupt(digitalPinToInterrupt(button), lcd_state, CHANGE);
  
  mcp2515.reset();
  mcp2515.setBitrate(CAN_125KBPS, MCP_8MHZ);
  mcp2515.setNormalMode();
}

void loop()
{
  //  currentTime = millis();
  if (Serial.available())
  {
    int incomingByte = Serial.read();
    hizBoleni = incomingByte / 10.0;
  }

  // Araçtan gelen değerler bölünerek USB Üzerine yazılıyor.
  // Eğer araçtan bir bilgi yukarı gelecek ise bunu Can_ID'si üzerinden belirtmeniz gerekir.
  if (mcp2515.readMessage(&canRcv) == MCP2515::ERROR_OK)
  {
    if (canRcv.can_id == 0x03)
    {
      doubler.array[0] = canRcv.data[0];
      doubler.array[1] = canRcv.data[1];
      doubler.array[2] = canRcv.data[2];
      doubler.array[3] = canRcv.data[3];
      Serial.print('b'); // basinc belirteci
      Serial.println(doubler.number);
      basinc_deger = doubler.number;
      doubler.array[0] = canRcv.data[4];
      doubler.array[1] = canRcv.data[5];
      doubler.array[2] = canRcv.data[6];
      doubler.array[3] = canRcv.data[7];
      Serial.print('s'); // sicaklik belirteci
      Serial.println(doubler.number);
      sicak_deger = doubler.number;
    }
  }
  else {
    //Serial.println("hata");
  }

  // Analogread 0-1023 arasında okuma yapar, burada esc değerleri olan 1000-2000 arasına eşitleniyor.
  // Herhangi bir joystick değerini 3000'den çıkarmak, joystick eksenini ters çevirme anlamına gelir.
  valueJoyStick_X_1 = analogRead(pinJoyStick_X_1) + 1000;
  valueJoyStick_Y_1 = (analogRead(pinJoyStick_Y_1) + 1000); //Buradaki 3000'i sildik. Eklenebilir. (3000 - ....)
  valueJoyStick_X_2 = (analogRead(pinJoyStick_X_2) + 1000); //Buradaki 3000'i sildik. Eklenebilir.
  valueJoyStick_Y_2 = 3000 - (analogRead(pinJoyStick_Y_2) + 1000);
  
  // Joystick değerlerini merkezi değiştirmeden bölme işlemleri
  valueJoyStick_X_1 = 1500 + (valueJoyStick_X_1 - 1500) / hizBoleni;
  valueJoyStick_Y_1 = 1500 + (valueJoyStick_Y_1 - 1500) / hizBoleni;
  valueJoyStick_X_2 = 1500 + (valueJoyStick_X_2 - 1500) / hizBoleni;
  valueJoyStick_Y_2 = 1500 + (valueJoyStick_Y_2 - 1500) / hizBoleni;

  if (valueJoyStick_X_1 > maxdeger) valueJoyStick_X_1 = maxdeger;
  if (valueJoyStick_Y_1 > maxdeger) valueJoyStick_Y_1 = maxdeger;
  if (valueJoyStick_X_2 > maxdeger) valueJoyStick_X_2 = maxdeger;
  if (valueJoyStick_Y_2 > maxdeger) valueJoyStick_Y_2 = maxdeger;

  if (valueJoyStick_X_1 < mindeger) valueJoyStick_X_1 = mindeger;
  if (valueJoyStick_Y_1 < mindeger)valueJoyStick_Y_1 = mindeger;
  if (valueJoyStick_X_2 < mindeger) valueJoyStick_X_2 = mindeger;
  if (valueJoyStick_Y_2 < mindeger)valueJoyStick_Y_2 = mindeger;

  // joystick'ler belli bi toleransla ortadayken 1500'e sabitliyoruz
  if (valueJoyStick_X_1 < 1500 + sabitleme_toleransi / hizBoleni && valueJoyStick_X_1 > 1500 - sabitleme_toleransi / hizBoleni)
    valueJoyStick_X_1 = 1500;
  if (valueJoyStick_Y_1 < 1500 + sabitleme_toleransi / hizBoleni && valueJoyStick_Y_1 > 1500 - sabitleme_toleransi / hizBoleni)
    valueJoyStick_Y_1 = 1500;
  if (valueJoyStick_X_2 < 1500 + sabitleme_toleransi / hizBoleni && valueJoyStick_X_2 > 1500 - sabitleme_toleransi / hizBoleni)
    valueJoyStick_X_2 = 1500;
  if (valueJoyStick_Y_2 < 1500 + sabitleme_toleransi / hizBoleni && valueJoyStick_Y_2 > 1500 - sabitleme_toleransi / hizBoleni)
    valueJoyStick_Y_2 = 1500;
    
  // Joystick degerleri 8 byte'a siralanip yollaniyor
  canSend.can_id = 0x02;
  canSend.can_dlc = 8;
  canSend.data[0] = highByte(valueJoyStick_X_1);
  canSend.data[1] = lowByte(valueJoyStick_X_1);
  canSend.data[2] = highByte(valueJoyStick_Y_1);
  canSend.data[3] = lowByte(valueJoyStick_Y_1);
  canSend.data[4] = highByte(valueJoyStick_X_2);
  canSend.data[5] = lowByte(valueJoyStick_X_2);
  canSend.data[6] = highByte(valueJoyStick_Y_2);
  canSend.data[7] = lowByte(valueJoyStick_Y_2);

  // LCD'ye yazı yazdırma
  if (!lcd_durum)
  {
    if (clear_state == true) lcd.clear();
    clear_state = false;
    lcd.home();
    lcd.print("Basinc:");
    lcd.setCursor(8, 0);
    lcd.print(basinc_deger);
    lcd.setCursor(0, 1);
    lcd.print("Sicaklik:");
    lcd.setCursor(10, 1);
    lcd.print(sicak_deger);
  }
  if (lcd_durum)
  {
    if (clear_state == true) lcd.clear();
    clear_state = false;
    lcd.home();
    lcd.print("x1:");
    lcd.setCursor(3, 0);
    lcd.print(valueJoyStick_X_1);
    lcd.setCursor(8, 0);
    lcd.print("x2:");
    lcd.setCursor(11, 0);
    lcd.print(valueJoyStick_X_2);
    lcd.setCursor(0, 1);
    lcd.print("y2:");
    lcd.setCursor(3, 1);
    lcd.print(valueJoyStick_Y_2);
    lcd.setCursor(8, 1);
    lcd.print("%");
    if (dis_nem < 10)
    {
      lcd.setCursor(9, 1);
      lcd.print("0");
      lcd.setCursor(10, 1);
      lcd.print(dis_nem);
    }
    else
    {
      lcd.setCursor(9, 1);
      lcd.print(dis_nem);
    }
    if (dis_sicaklik < 10)
    {
      lcd.setCursor(12, 1);
      lcd.print("0");
      lcd.setCursor(13, 1);
      lcd.print(dis_sicaklik);
    }
    else
    {
      lcd.setCursor(12, 1);
      lcd.print(dis_sicaklik);
    }
    lcd.setCursor(14, 1);
    lcd.print("C");
  }
  mcp2515.sendMessage(&canSend);
  delay(20);
}

// Bu fonksiyonu düzenlilik için alta aldım, umarım sorun olmaz
void lcd_state()
{
  if (lcd_durum == false) lcd_durum = true;
  else lcd_durum = false;
  clear_state = true;
  Serial.println(lcd_durum);
}
