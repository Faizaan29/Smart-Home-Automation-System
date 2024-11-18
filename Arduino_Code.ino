void setup() {
    Serial.begin(9600); // Start Serial Communication
    pinMode(2, OUTPUT); // Relay connected to pin 2
}

void loop() {
    if (Serial.available()) {
        char command = Serial.read(); // Read command from Raspberry Pi
        if (command == '1') {
            digitalWrite(2, HIGH); // Turn on the appliance
        } else if (command == '0') {
            digitalWrite(2, LOW); // Turn off the appliance
        }
    }
    delay(100);
}
