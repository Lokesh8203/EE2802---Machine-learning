#include "Arduino.h"
#include <math.h>
#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup()
{
    Serial.begin(9600);
    lcd.begin(16, 2);
}

void loop()
{
    int sensorValue = analogRead(A0);             // resistance
    double voltage = ((3.3 * sensorValue) / 666); // voltage divider rule
    // double a = 0.0000012524;
    double b = 0.00291;
    double c = (-1.48 + voltage);

    //  double Temp = (- b + sqrt((b*b - 4*a*c)))/ (2*a) ;
    double Temp = c / b;
    Serial.println(sensorValue);
    Serial.println(voltage);
    Serial.println(Temp);
    lcd.print("Temp(in Celcius)");
    lcd.setCursor(1, 2);
    lcd.print(Temp);
    delay(1000);
    lcd.clear();
}