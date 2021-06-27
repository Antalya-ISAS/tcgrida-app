
unsigned long currentTime;
unsigned long firstClick;
unsigned long secondClick;
byte butonPin = 2;
int buttonDurum = 0;
unsigned long limit = 1000;
void setup() {
  Serial.begin(9600);
  pinMode(butonPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(butonPin), Ahmet, RISING);
}

void loop() {

  currentTime = millis();
  unsigned long sonuc = secondClick - firstClick;
  if(buttonDurum && sonuc >= limit)
  {
    Serial.println("Hi");
    buttonDurum = 0;
  }
  //Serial.println("adfsdf");
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
  buttonDurum++;
  if(buttonDurum%2 == 1)
  {
    firstClick = currentTime;
  }
  if(buttonDurum%2 == 0)
  {
    secondClick = currentTime;
  }
}
