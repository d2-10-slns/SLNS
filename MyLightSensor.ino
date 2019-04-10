void setup()
{
  // Set pin 5 as an input pin
  pinMode(5,INPUT);
  // Start up serial communication with a speed of 9600
  Serial.begin(9600);
}

void loop()
{
  // Read in the current value of the light sensor
  int reading = analogRead(5);
  // Send the value that we just read down the serial connection
  Serial.println(reading);
  // Wait for a bit, just to slow everything down
  delay(500);
}
