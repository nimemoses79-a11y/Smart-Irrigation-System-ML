const int sensorPin = A0;
const int relayPin = 7;

// Active-LOW relay
bool pumpOn = false;

void setup() {
  Serial.begin(9600);
  pinMode(relayPin, OUTPUT);

  // Start with pump OFF
  digitalWrite(relayPin, HIGH);
}

void loop() {
  // Send live moisture reading to Python
  static unsigned long lastReading = 0;

  if (millis() - lastReading >= 1000) {
    lastReading = millis();

    int moisture = analogRead(sensorPin);

    Serial.print("MOISTURE,");
    Serial.println(moisture);
  }

  // Receive pump command from Python
  while (Serial.available() > 0) {
    char command = Serial.read();

    if (command == '1') {
      pumpOn = true;
    }
    else if (command == '0') {
      pumpOn = false;
    }
  }

  // Active-LOW relay: LOW = ON, HIGH = OFF
  digitalWrite(relayPin, pumpOn ? LOW : HIGH);
}