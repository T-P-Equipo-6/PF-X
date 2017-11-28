#include <Wire.h>

int buzzerPin = 8;
int alarmLeds = 9;
int counter = 0;

bool trigger = false;

int note = 880;
int duration = 500;
 
void setup() {
  Serial.begin(115200);
  
  pinMode(buzzerPin, OUTPUT);
  pinMode(alarmLeds, OUTPUT);
  digitalWrite(buzzerPin, LOW);
  digitalWrite(alarmLeds, LOW);
  
  Wire.begin(1);
  Wire.onReceive(receiveEvent);
}
 
void loop() {
  if (trigger == false){
    return
  }
  else{
    tone(buzzerPin, note, duration);
    if(counter % 2 == 0){
      digitalWrite(alarmLeds, HIGH);
      delay(duration);
    }else{
      digitalWrite(alarmLeds, LOW);
      delay(duration);
    }
      noTone(buzzerPin);
      delay(50);

      counter++;
  }
}

void receiveEvent(int state) {
  trigger = Wire.read() == 1 ? true : false;
}
