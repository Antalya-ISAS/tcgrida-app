#include "Wire.h"
#include <MPU6050_light.h>
#include <Servo.h>
#include "mcp2515.h"

#define maxdeger 1940 
#define mindeger 1060
//Motorları tersine çevirmek için açıklama satırlarını iptal edin
#define TERSONSAG
#define TERSONSOL
//#define TERSARKASOL 
//#define TERSARKASAG 

//ÖLÜ NOKTA
#define sabitleme_toleransi 10

struct can_frame canMsg; // gelen mesaj
struct can_frame canSnd; // giden mesaj

MCP2515 mcp2515(8);
MPU6050 mpu(Wire);

int valueJoyStick_X_1 = 0;
int valueJoyStick_Y_1 = 0;
int valueJoyStick_X_2 = 0;
int valueJoyStick_Y_2 = 0;

Servo yukselis, onsa, onso, arsa, arso; //yukselis sag, yukselis sol...

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

//PID constants
double kp = 2
double ki = 5
double kd = 1
 
unsigned long currentTime, previousTime;
double elapsedTime;
double error;
double lastError;
double input, output, setPoint;
double cumError, rateError;
double xValue;
double yValue;

void setup() 
{
    Serial.begin(115200);
    Serial.println("Basladi.");
    SPI.begin();

    //canbus
    mcp2515.reset();
    mcp2515.setBitrate(CAN_125KBPS,MCP_8MHZ);
    mcp2515.setNormalMode();

    Wire.begin();
    byte status = mpu.begin();
    Serial.print(F("MPU6050 status: "));
    Serial.println(status);
    while(status!=0){ } // stop everything if could not connect to MPU6050
    Serial.println(F("Calculating offsets, do not move MPU6050"));
    delay(1000);
    mpu.calcOffsets(true,true); // gyro and accelero
    Serial.println("Done!\n");

    //servos
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
            yukselis.writeMicroseconds(valueJoyStick_X_1);
            onsa_deger = 1500 + (valueJoyStick_X_2 - 1500) - (valueJoyStick_Y_2 - 1500);
            onso_deger = 1500 + (valueJoyStick_X_2 - 1500) + (valueJoyStick_Y_2 - 1500);
            arsa_deger = 1500 + (valueJoyStick_X_2 - 1500) - (valueJoyStick_Y_2 - 1500);
            arso_deger = 1500 + (valueJoyStick_X_2 - 1500) + (valueJoyStick_Y_2 - 1500); 

            //error correction
            /*
            mpu.update();
            xValue = mpu.getAngleX();
            yValue = mpu.getAngleY();
            outputX = ComputePID(xValue, valueJoystick_X_2); //currentpoint vs. setpoint
            outputY = ComputePID(yValue, valueJoystick_Y_2); //currentpoint vs. setpoint
            onsa_deger = 1500 + (outputX - 1500) - (outputY - 1500); 
            onso_deger = 1500 + (outputX - 1500) + (outputY - 1500);
            arsa_deger = 1500 + (outputX - 1500) - (outputY - 1500);
            arso_deger = 1500 + (outputX - 1500) + (outputY - 1500);
            */

            // Ölü nokta
            if (onsa_deger < 1500 + sabitleme_toleransi && onsa_deger > 1500 - sabitleme_toleransi)
              onsa_deger = 1500;
            if (onso_deger < 1500 + sabitleme_toleransi && onso_deger > 1500 - sabitleme_toleransi)
              onso_deger = 1500;
            if (arsa_deger < 1500 + sabitleme_toleransi && arsa_deger > 1500 - sabitleme_toleransi)
              arsa_deger = 1500;
            if (arso_deger < 1500 + sabitleme_toleransi && arso_deger > 1500 - sabitleme_toleransi)
              arso_deger = 1500;
            
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
              yukselis.writeMicroseconds(1000); //bağlantı alınmazsa denizin yüzeyine çık 
              onsa.writeMicroseconds(1500);
              onso.writeMicroseconds(1500);
              arsa.writeMicroseconds(1500);
              arso.writeMicroseconds(1500);
              lasttime=currenttime;
    }
}

double computePID(double currentPoint, double setPoint)
{     
    currentTime = millis();
    elapsedTime = (double)(currentTime - previousTime);
        
    error = setPoint - currentPoint; 
    cumError += error * elapsedTime; // compute integral
    rateError = (error - lastError)/elapsedTime; // compute derivative
 
    double out = kp*error + ki*cumError + kd*rateError; //PID output               
 
    lastError = error; //remember current error
    previousTime = currentTime; //remember current time
 
    return out;
}
