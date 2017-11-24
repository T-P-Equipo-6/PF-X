int UltrasonicSensor1Out = 2;
int UltrasonicSensor1In = 3;
int UltrasonicSensor2Out = 4;
int UltrasonicSensor2In = 5;
int bedroom = 13;
int kitchen = 12;
int livingroom = 11;
int studio = 10;
int TempSensorPin = A0;
int buzzerPin = 8;
int alarmLeds = 9;
int counter = 0;

const int c = 261;
const int d = 294;
const int e = 329;
const int f = 349;
const int g = 391;
const int gS = 415;
const int a = 440;
const int aS = 455;
const int b = 466;
const int cH = 523;
const int cSH = 554;
const int dH = 587;
const int dSH = 622;
const int eH = 659;
const int fH = 698;
const int fSH = 740;
const int gH = 784;
const int gSH = 830;
const int aH = 880;

String inCommand = "";

void setup() {
  Serial.begin(115200);
  pinMode(bedroom, OUTPUT);
  pinMode(kitchen, OUTPUT);
  pinMode(livingroom, OUTPUT);
  pinMode(studio, OUTPUT);
  pinMode(UltrasonicSensor1Out, OUTPUT);
  pinMode(UltrasonicSensor1In, INPUT);
  pinMode(UltrasonicSensor2Out, OUTPUT);
  pinMode(UltrasonicSensor2In, INPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(alarmLeds, OUTPUT);
  digitalWrite(UltrasonicSensor1Out, LOW);
  digitalWrite(UltrasonicSensor1In, LOW);
  digitalWrite(UltrasonicSensor2Out, LOW);
  digitalWrite(UltrasonicSensor2In, LOW);
  digitalWrite(bedroom, LOW);
  digitalWrite(kitchen, LOW);
  digitalWrite(livingroom, LOW);
  digitalWrite(studio, LOW);
  digitalWrite(buzzerPin, LOW);
  digitalWrite(alarmLeds, LOW);
}

void loop() {
  float UltrasonicSensorValue1 = readUltrasonicSensorValue(UltrasonicSensor1Out, UltrasonicSensor1In);
  float UltrasonicSensorValue2 = readUltrasonicSensorValue(UltrasonicSensor2Out, UltrasonicSensor2In);
  float TempSensorValue = readTempSensorValue();
  sendData(UltrasonicSensorValue1, UltrasonicSensorValue2, TempSensorValue);
}

void sendData(float UltrasonicSensorValue1, float UltrasonicSensorValue2, float TempSensorValue) {
  Serial.print("{\"UltrasonicSensorValue1\": ");
  Serial.print("\"UltrasonicSensorValue1\"");
  Serial.print(", ");
  Serial.print("\"UltrasonicSensorValue2\": ");
  Serial.print("\"UltrasonicSensorValue2\"");
  Serial.print(", ");
  Serial.print("\"TempSensorValue\": ");
  Serial.print("\"TempSensorValue\"");
  Serial.println("}");
  delay(100);
}

float readUltrasonicSensorValue(int Out, int In) {
  digitalWrite(Out, LOW);
  digitalWrite(In, LOW);
  digitalWrite(Out, HIGH);
  delayMicroseconds(10);
  float timeRead = pulseIn(In, HIGH);
  return timeRead;
}

float readTempSensorValue() {
  int sensorValue = analogRead(TempSensorPin);
  return sensorValue;
}

void serialEvent() {
  inCommand = Serial.readStringUntil("\r\n");
  if (inCommand == "LIGHTSBEDROOMON"){
    digitalWrite(bedroom, HIGH);
  }
  if (inCommand == "LIGHTSBEDROOMOFF"){
    digitalWrite(bedroom, LOW);
  }
  if (inCommand == "LIGHTSSTUDIOON"){
    digitalWrite(studio, HIGH);
  }
  if (inCommand == "LIGHTSSTUDIOOFF"){
    digitalWrite(studio, LOW);
  }
  if (inCommand == "LIGHTSKITCHENON"){
    digitalWrite(kitchen, HIGH);
  }
  if (inCommand == "LIGHTSKITCHENOFF"){
    digitalWrite(kitchen, LOW);
  }
  if (inCommand == "LIGHTSLIVINGROOMON"){
    digitalWrite(livingroom, HIGH);
  }
  if (inCommand == "LIGHTSLIVINGROOMOFF"){
    digitalWrite(livingroom, LOW);
  }
  if (inCommand == "ALARMON"){
    triggerAlarm();
  }
  if (inCommand == "ALARMOFF"){
  }
}

void triggerAlarm() {
  digitalWrite(bedroom, LOW);
  digitalWrite(kitchen, LOW);
  digitalWrite(livingroom, LOW);
  digitalWrite(studio, LOW);
  playAlarmSong();
}

void playAlarmSong() {
  firstSection();

  secondSection();

  beep(f, 250);  
  beep(gS, 500);  
  beep(f, 350);  
  beep(a, 125);
  beep(cH, 500);
  beep(a, 375);  
  beep(cH, 125);
  beep(eH, 650);
 
  delay(500);

  secondSection();

  beep(f, 250);  
  beep(gS, 500);  
  beep(f, 375);  
  beep(cH, 125);
  beep(a, 500);  
  beep(f, 375);  
  beep(cH, 125);
  beep(a, 650);  
 
  delay(650);
}

void beep(int note, int duration) {
  tone(buzzerPin, note, duration);
  if(counter % 2 == 0)
  {
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

void firstSection() {
  beep(a, 500);
  beep(a, 500);    
  beep(a, 500);
  beep(f, 350);
  beep(cH, 150);  
  beep(a, 500);
  beep(f, 350);
  beep(cH, 150);
  beep(a, 650);
 
  delay(500);
 
  beep(eH, 500);
  beep(eH, 500);
  beep(eH, 500);  
  beep(fH, 350);
  beep(cH, 150);
  beep(gS, 500);
  beep(f, 350);
  beep(cH, 150);
  beep(a, 650);
 
  delay(500);
}
 
void secondSection() {
  beep(aH, 500);
  beep(a, 300);
  beep(a, 150);
  beep(aH, 500);
  beep(gSH, 325);
  beep(gH, 175);
  beep(fSH, 125);
  beep(fH, 125);    
  beep(fSH, 250);
 
  delay(325);
 
  beep(aS, 250);
  beep(dSH, 500);
  beep(dH, 325);  
  beep(cSH, 175);  
  beep(cH, 125);  
  beep(b, 125);  
  beep(cH, 250);  
 
  delay(350);
}

