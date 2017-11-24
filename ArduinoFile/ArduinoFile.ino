int UltrasonicSensor1Out = 2;
int UltrasonicSensor1In = 3;
int UltrasonicSensor2Out = 4;
int UltrasonicSensor2In = 5;
int led1 = 13;
int led2 = 12;
int led3 = 11;
int led4 = 10;

void setup() {
  Serial.begin(115200);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  digitalWrite(led4, LOW);
}

void loop() {
  float UltrasonicSensorValue1 = readUltrasonicSensorValue(UltrasonicSensor1Out, UltrasonicSensor1In);
  float UltrasonicSensorValue2 = readUltrasonicSensorValue(UltrasonicSensor2Out, UltrasonicSensor2In);
  sendData(UltrasonicSensorValue1, UltrasonicSensorValue2);
}

void sendData(float UltrasonicSensorValue1, float UltrasonicSensorValue2) {
  Serial.print("{'UltrasonicSensorValue1': ");
  Serial.print(UltrasonicSensorValue1);
  Serial.print(", ");
  Serial.print("'UltrasonicSensorValue2': ");
  Serial.print(UltrasonicSensorValue2);
  Serial.println("}");
}

float readUltrasonicSensorValue(int Out, int In) {
  digitalWrite(Out, HIGH);
  delayMicroseconds(10);
  float timeRead = pulseIn(In, HIGH);
  return timeRead;
}

void serialEvent() {
  char inChar = (char)Serial.read();
  int state1 = inChar == '1' ? HIGH : LOW;
  int state2 = inChar == '2' ? HIGH : LOW;
  int state3 = inChar == '3' ? HIGH : LOW;
  int state4 = inChar == '4' ? HIGH : LOW;
  digitalWrite(led1, state1);
  digitalWrite(led2, state2);
  digitalWrite(led3, state3);
  digitalWrite(led4, state4);
}

