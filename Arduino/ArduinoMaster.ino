#include <Wire.h>

int UltrasonicSensor1Out = 2;
int UltrasonicSensor1In = 3;
int UltrasonicSensor2Out = 4;
int UltrasonicSensor2In = 5;
int fan = 6;
int bedroom = 10;
int kitchen = 11;
int livingroom = 12;
int studio = 13;
int TempSensorPin = A0;

int state = 0;

String inCommand = "";

void setup() {
  Serial.begin(115200);
  
  pinMode(bedroom, OUTPUT);
  pinMode(kitchen, OUTPUT);
  pinMode(livingroom, OUTPUT);
  pinMode(studio, OUTPUT);
  pinMode(fan, OUTPUT);
  pinMode(UltrasonicSensor1Out, OUTPUT);
  pinMode(UltrasonicSensor1In, INPUT);
  pinMode(UltrasonicSensor2Out, OUTPUT);
  pinMode(UltrasonicSensor2In, INPUT);
  digitalWrite(UltrasonicSensor1Out, LOW);
  digitalWrite(UltrasonicSensor1In, LOW);
  digitalWrite(UltrasonicSensor2Out, LOW);
  digitalWrite(UltrasonicSensor2In, LOW);
  digitalWrite(bedroom, LOW);
  digitalWrite(kitchen, LOW);
  digitalWrite(livingroom, LOW);
  digitalWrite(studio, LOW);
  digitalWrite(fan, LOW);
  
  Wire.begin();
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
  if (inCommand == "FANHOUSEON"){
    digitalWrite(fan, HIGH);
  }
  if (inCommand == "FANHOUSEOFF"){
    digitalWrite(fan, LOW);
  }
  if (inCommand == "ALARMON"){
    state = 1;

    digitalWrite(bedroom, LOW);
    digitalWrite(kitchen, LOW);
    digitalWrite(livingroom, LOW);
    digitalWrite(studio, LOW);
    Wire.beginTransmission(1);
    Wire.write(state);
    Wire.endTransmission();
  }
  if (inCommand == "ALARMOFF"){
    state = 0;

    Wire.beginTransmission(1);
    Wire.write(state);
    Wire.endTransmission();
  }
}

