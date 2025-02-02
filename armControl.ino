#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;
Servo servo7;

int pos = 0;

void setup() {
  servo1.attach(3);
  servo2.attach(5);
  servo3.attach(6);
  servo4.attach(9);
  servo5.attach(10);
  servo6.attach(11);
  servo7.attach(12);

  Serial.begin(9600);
}

void initPosition()
{
  //initial position 
  servo1.write(155);
  servo2.write(100);
  servo3.write(80);
  servo4.write(70);
  servo5.write(85);
  servo6.write(160);
  servo7.write(100);
  delay(1000);
}


void moveToConveyor()
{
  //move to conveyor
  for(int i=100; i>83; i--)
  {
    servo2.write(i);
    delay(20);
  }
  for(int i=80; i<165; i++)
  {
    servo3.write(i);
    delay(20);
  }
  for(int i=85; i>10; i--)
  {
    servo5.write(i);
    delay(20);
  }
  delay(1000);
}


void grab()
{
  servo6.write(0);
  delay(1000);
}

void drop()
{
  servo6.write(160);
  delay(1000);
}

void move(int bin)
{
  for(int i=75; i<130; i++)
  {
    servo2.write(i);
    delay(20);
  }
  for(int i=165; i>0; i--)
  {
    servo3.write(i);
    delay(20);
  }
  for(int i=0; i<170; i++)
  {
    servo5.write(i);
    delay(20);
  }

  if(bin==1)
  {}  
  else if(bin==2)
  {
    for(int i=155; i>125; i--)
    {
      servo1.write(i);
      delay(20);
    }
  }
  else if(bin==3)
  {
    for(int i=155; i>100; i--)
    {
      servo1.write(i);
      delay(20);
    }
  }
  else if(bin==4)
  {
    for(int i=155; i>75; i--)
    {
      servo1.write(i);
      delay(20);
    }
  }
  else if(bin==5)
  {
    for(int i=155; i>40; i--)
    {
      servo1.write(i);
      delay(20);
    }
  }
  else if(bin==6)
  {
    for(int i=155; i>10; i--)
    {
      servo1.write(i);
      delay(20);
    }
  }
  delay(1000);
}

void loop() {

  
  if (Serial.available() > 0) {
    // Read the incoming byte and store it in a variable
    String incomingData = Serial.readStringUntil('\n');
   
    // Print the received data to the Serial Monitor (optional)
    Serial.print("Received: ");
    Serial.println(incomingData);
    Serial.flush();
   
    if (incomingData == "box1") {
      initPosition();
      moveToConveyor();
      grab();
      move(1);
      drop();
      delay(1000);
    }
    if (incomingData == "box2") {
      initPosition();
      moveToConveyor();
      grab();
      move(2);
      drop();
      delay(1000);
    }
    if (incomingData == "box3") {
      initPosition();
      moveToConveyor();
      grab();
      move(3);
      drop();
      delay(1000);
    }
    if (incomingData == "box4") {
      initPosition();
      moveToConveyor();
      grab();
      move(4);
      drop();
      delay(1000);
    }
    if (incomingData == "box5") {
      initPosition();
      moveToConveyor();
      grab();
      move(5);
      drop();
      delay(1000);
    }
    if (incomingData == "box6") {
      initPosition();
      moveToConveyor();
      grab();
      move(6);
      drop();
      delay(1000);
    }
   
    // Optionally, add a small delay
    delay(100);
 
  }


}

