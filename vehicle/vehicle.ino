
#include <Servo.h>
#include <mcp2515.h>

#define maxdeger 1940 //max 2000 oluyor escler 1000-2000 arası calisir
#define mindeger 1060
//Motorları tersine çevirmek için açıklama satırlarını iptal edin
//#define TERSONSAG
#define TERSONSOL
//#define TERSARKASOL 
#define TERSARKASAG 

struct can_frame canMsg; // gelen mesaj
struct can_frame canSnd; // giden mesaj

MCP2515 mcp2515(8);

int valueJoyStick_X_1 = 0;
int valueJoyStick_Y_1 = 0;
int valueJoyStick_X_2 = 0;
int valueJoyStick_Y_2 = 0;


Servo yukselis, onsa, onso, arsa, arso;

int yuk_deger, onsa_deger, onso_deger, arsa_deger, arso_deger;

int canbus_deadline=1000;
int lasttime,currenttime;

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
    Serial.begin(115200);
    Serial.println("Basladi.");
    SPI.begin();


    mcp2515.reset();
    mcp2515.setBitrate(CAN_125KBPS,MCP_8MHZ);
    mcp2515.setNormalMode();

    yukselis.attach(10, 1000, 2000);
    onsa.attach(9, 1000, 2000);
    onso.attach(5, 1000, 2000);
    arsa.attach(6, 1000, 2000);
    arso.attach(3, 1000, 2000);

              
              
}

void loop()
{
currenttime=millis();
    if (mcp2515.readMessage(&canMsg) == MCP2515::ERROR_OK)
    {
    Serial.print(canMsg.can_id, HEX); // print ID
    Serial.print(" "); 
    Serial.print(canMsg.can_dlc, HEX); // print DLC
    Serial.print(" ");

    for (int i = 0; i<canMsg.can_dlc; i++)  {  // print the data
      Serial.print(canMsg.data[i],HEX);
      Serial.print(" ");
    }
        if (canMsg.can_id == 0x02)
        {
            for (int i = 0; i < canMsg.can_dlc; i += 2)
            {
                converter.array[1] = canMsg.data[i];
                converter.array[0] = canMsg.data[i + 1];
                if (i == 0)
                    valueJoyStick_X_1 = converter.integer;
                else if (i == 2)
                    valueJoyStick_Y_1 = converter.integer;
                else if (i == 4)
                    valueJoyStick_X_2 = converter.integer;
                else if (i == 6)
                    valueJoyStick_Y_2 = converter.integer;
            }

            //Joystick değerlerinin anlamlı verilere dönüştürülmesi
            // Bu kısım itici dizilimine göre değiştirilir.
            // Joystickleri analiz edip her motor için etkisinin + ve - değerleri ile belirlenmesi gereklidir.
            yukselis.writeMicroseconds(3000-valueJoyStick_X_1);
            onsa_deger = 1500 + (valueJoyStick_X_2 - 1500) - (valueJoyStick_Y_2 - 1500);
            onso_deger = 1500 + (valueJoyStick_X_2 - 1500) + (valueJoyStick_Y_2 - 1500);
            arsa_deger = 1500 + (valueJoyStick_X_2 - 1500) - (valueJoyStick_Y_2 - 1500);
            arso_deger = 1500 + (valueJoyStick_X_2 - 1500) + (valueJoyStick_Y_2 - 1500);
            #ifdef TERSONSOL
            onso_deger=3000-onso_deger;
            #endif
            #ifdef TERSONSAG
            onsa_deger=3000-onsa_deger;
            #endif
            #ifdef TERSARKASOL
            arso_deger=3000-arso_deger;
            #endif
            #ifdef TERSARKASAG
            arsa_deger=3000-arsa_deger;
            #endif
            Serial.println(onsa_deger);
            Serial.println(onso_deger);
            Serial.println(arsa_deger);
            Serial.println(arso_deger);
            
            if (onsa_deger >= maxdeger) onsa_deger = maxdeger;
            else if (onsa_deger <= mindeger) onsa_deger = mindeger;
            if (arsa_deger >= maxdeger) arsa_deger = maxdeger;
            else if (arsa_deger <= mindeger) arsa_deger = mindeger;
            if (onso_deger >= maxdeger) onso_deger = maxdeger;
            else if (onso_deger <= mindeger) onso_deger = mindeger;
            if (arso_deger >= maxdeger) arso_deger = maxdeger;
            else if (arso_deger <= mindeger) arso_deger = mindeger;
              onsa.writeMicroseconds(onsa_deger);
              onso.writeMicroseconds(onso_deger);
              arsa.writeMicroseconds(arsa_deger);
              arso.writeMicroseconds(arso_deger);
            delay(5);
            
            Serial.print(valueJoyStick_X_1);
            Serial.print("--");
            Serial.print(valueJoyStick_Y_1);
            Serial.print("--");
            Serial.print(valueJoyStick_X_2);
            Serial.print("--");
            Serial.print(valueJoyStick_Y_2);
            Serial.println("--"); 
            
        }
        lasttime=currenttime;
    }
    else if(currenttime-lasttime>canbus_deadline)
    {
              yukselis.writeMicroseconds(1000);
              onsa.writeMicroseconds(1500);
              onso.writeMicroseconds(1500);
              arsa.writeMicroseconds(1500);
              arso.writeMicroseconds(1500);
              lasttime=currenttime;
    }
}
