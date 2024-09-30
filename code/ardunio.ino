#include <Servo.h>

Servo myservo;

#define S0 26
#define S1 25
#define S2 24
#define S3 23
#define sensorOut 22

const int Ena = 2;
const int in1 = 3;
const int in2 = 4;
const int buttonPin = 5;

int redFrequency = 0;
int greenFrequency = 0;
int blueFrequency = 0;

void setup() {
  pinMode(Ena, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);

  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(sensorOut, INPUT);

  digitalWrite(S0, HIGH);
  digitalWrite(S1, LOW);

  myservo.attach(27);
  myservo.write(90);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(buttonPin) == LOW) {
    while (true) {
      if (Serial.available() > 0) {
        handleCommand(Serial.read());
      } else {
        stopMotors(); // إذا لم يكن هناك أوامر، توقف عن الحركة
      }
      readColor();
    }
  }
}

void handleCommand(char command) {
  if (command == '1') {
    myservo.write(90);
    driveForward();
  } else if (command == '2') {
    myservo.write(0);
    driveForward();
  } else if (command == '3') {
    myservo.write(0);
    waitForCommand('1');
  } else if (command == '4') {
    myservo.write(180);
    waitForCommand('5');
  } else if (command == '6') {
    myservo.write(0);
    waitForCommand('6');
  } else if (command == '0') {
    myservo.write(90);
    stopMotors();
  }
}

void waitForCommand(char expected) {
  while (true) {
    if (Serial.available() > 0 && Serial.read() == expected) break;
  }
}

void driveForward() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  analogWrite(Ena, 220);
}

void stopMotors() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  analogWrite(Ena, 0);
}

void readColor() {
  digitalWrite(S2, LOW);
  digitalWrite(S3, LOW);
  redFrequency = pulseIn(sensorOut, LOW);
  
  digitalWrite(S2, HIGH);
  digitalWrite(S3, HIGH);
  greenFrequency = pulseIn(sensorOut, LOW);
  
  digitalWrite(S2, LOW);
  digitalWrite(S3, HIGH);
  blueFrequency = pulseIn(sensorOut, LOW);
  
  if (redFrequency < 20 && greenFrequency > 22 && blueFrequency > 22) {
    myservo.write(40);
  } else if (redFrequency > 20 && greenFrequency > 22 && blueFrequency > 22) {
    myservo.write(40);
    delay(500);
    myservo.write(90);
  }
}