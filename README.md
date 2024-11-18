# Smart Home Automation System

This project integrates a **Raspberry Pi**, **Arduino UNO**, and various components for home automation.

## Features
- Control appliances via a relay module connected to the Arduino.
- Serial communication between Raspberry Pi and Arduino for commands.
- Simple Python script for controlling appliances.

## Components Used
- **Raspberry Pi** as the central hub.
- **Arduino UNO** for handling relays and sensor data.
- **Relay module** for appliance control.
- **Wi-Fi module (ESP8266)** for future integration (optional).

## How to Run
1. Upload `Arduino_Code.ino` to your Arduino UNO.
2. Run `/main.py` on your Raspberry Pi or PC.
3. Use the console to send "ON" or "OFF" commands to control the appliance.
