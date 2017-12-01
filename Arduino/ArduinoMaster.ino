#include <Wire.h>

int UltrasonicSensor1Out = 7;
int UltrasonicSensor1In = 8;

int motorForwardPin = 9;
int motorBackwardPin = 10;

int bedroom = 2;
int studio = 3;
int kitchen = 4;
int bathroom = 5;
int fan = 6;

int TempSensorPin = A0;

int state = 0;

bool isOpen = false;

String inCommand = "";

void setup() {
  Serial.begin(9600);
  
  pinMode(bedroom, OUTPUT);
  pinMode(kitchen, OUTPUT);
  pinMode(bathroom, OUTPUT);
  pinMode(studio, OUTPUT);
  pinMode(fan, OUTPUT);
  
  pinMode(UltrasonicSensor1Out, OUTPUT);
  pinMode(UltrasonicSensor1In, INPUT);

  pinMode(motorForwardPin, OUTPUT);
  pinMode(motorBackwardPin, OUTPUT);
  
  digitalWrite(UltrasonicSensor1Out, LOW);
  digitalWrite(UltrasonicSensor1In, LOW);
  
  digitalWrite(bedroom, LOW);
  digitalWrite(kitchen, LOW);
  digitalWrite(bathroom, LOW);
  digitalWrite(studio, LOW);
  digitalWrite(fan, LOW);

  digitalWrite(motorForwardPin, LOW);
  digitalWrite(motorBackwardPin, LOW);
  
  Wire.begin();
}

void loop() {
  float UltrasonicSensorValue1 = readUltrasonicSensorValue(UltrasonicSensor1Out, UltrasonicSensor1In);
  float TempSensorValue = readTempSensorValue();
  sendData(UltrasonicSensorValue1, TempSensorValue);
}

void sendData(float UltrasonicSensorValue1, float temperatureValue) {
  Serial.print("{\"USV\": ");
  Serial.print(UltrasonicSensorValue1);
  Serial.print(", ");
  Serial.print("\"TEMP\": ");
  Serial.print(temperatureValue);
  Serial.println("}");
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
  if (inCommand == "LIGHTSBATHROOMON"){
    digitalWrite(bathroom, HIGH);
  }
  if (inCommand == "LIGHTSBATHROOMOFF"){
    digitalWrite(bathroom, LOW);
  }
  if (inCommand == "FANHOUSEON"){
    digitalWrite(fan, HIGH);
  }
  if (inCommand == "FANHOUSEOFF"){
    digitalWrite(fan, LOW);
  }
  if (inCommand == "DOORFRONTOPEN"){
    if (isOpen == false){
      digitalWrite(motorForwardPin, HIGH);
      digitalWrite(motorBackwardPin, LOW);
      delay(2000);
      digitalWrite(motorForwardPin, LOW);
      digitalWrite(motorBackwardPin, LOW);
      isOpen = true;
    }
  }
  if (inCommand == "DOORFRONTCLOSE"){
    if (isOpen = true){
      digitalWrite(motorForwardPin, LOW);
      digitalWrite(motorBackwardPin, HIGH);
      delay(2000);
      digitalWrite(motorForwardPin, LOW);
      digitalWrite(motorBackwardPin, LOW);
      isOpen = false;
    }
  }
  if (inCommand == "ALARMON"){
    state = 1;

    digitalWrite(bedroom, LOW);
    digitalWrite(kitchen, LOW);
    digitalWrite(bathroom, LOW);
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
