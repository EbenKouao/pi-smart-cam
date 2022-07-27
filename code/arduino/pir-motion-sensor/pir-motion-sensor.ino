/*     Creator: @Smartbuilds.io
 *     Date: 01.05.22
 *     
 *     Arduino PIR Camera Sensor
 *     Description: Arduino reads input/sensor value and communicates to the Raspberry Pi
*/

int pirSensor = 8; // Arduino Digital Pin 8

const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  5;      // the number of the LED pin
int buttonState = 0;         // button state 0 LOW, 1 HIGH

int pinStateCurrent = LOW; // current state of pin
int pinStatePrevious = LOW; // previous state of pin

void setup() {

  //  Initial PIR Sensor
  pinMode(pirSensor, INPUT);
  Serial.begin(9600);

  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);

  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  digitalWrite(ledPin, LOW);

}

void loop() {
  
  pinStatePrevious = pinStateCurrent; // store previous state of motion sensor
  pinStateCurrent = digitalRead(pirSensor);

  if (pinStatePrevious == LOW && pinStateCurrent == HIGH){
    
    Serial.write("1"); // Send message to the Raspberry pi - Motion Detected
    digitalWrite(ledPin, LOW);
    
  }else if (pinStatePrevious == HIGH && pinStateCurrent == LOW) { 
   
    Serial.println("0"); // Motion stopped - Send message to the Raspberry pi
    digitalWrite(ledPin, HIGH);

  }

}

// Create your own Button/Ring Button - When Pressed sends comms to the Pi to trigger an action

// read the state of the pushbutton value:
//  buttonState = digitalRead(buttonPin);

// check if the pushbutton is pressd i.e. the buttonState is HIGH:
//  if (buttonState == HIGH) {
//    // turn LED on:
//    Serial.write("ring-ring/"); // Send message to the Raspberry Pi
//    digitalWrite(ledPin, HIGH);
//    delay(3000);
//  } else {
//    // turn LED off:
//    digitalWrite(ledPin, LOW);
//  }

//}
