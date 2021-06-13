
unsigned long currentTime;
unsigned long previousTime;
byte butonPin = 2;
byte butonDurum = 0;
byte butonOncekiDurum = 1;
byte butonModDeger = 0;
unsigned long limit = 500;
void setup() {
  Serial.begin(9600);
  pinMode(butonPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(butonPin), Ahmet, RISING);
}

void loop() {

  currentTime = millis();
  unsigned long sonuc = currentTime - previousTime;
  if (butonDurum == 1 && sonuc >= limit)
  {
    Serial.println ("Ahmet");
    butonDurum = LOW;

  }
  //butonDurum = analogRead(buttonPin);
  //Serial.println(butonDurum);

  /* if(buttonDurum == LOW)
    {
    butonOncekiDurum=0;
    }


    if(butonOncekiDurum == LOW && buttonDurum == HIGH){
    Serial.println("Degisim algilandi");
    delay(1000);
    butonOncekiDurum=1;
    }*/

}
void Ahmet()
{
  previousTime = currentTime;
  butonDurum=1;
}
