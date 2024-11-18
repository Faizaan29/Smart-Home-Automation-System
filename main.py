import serial
import time

# Setup serial communication with Arduino
arduino = serial.Serial('COM3', 9600, timeout=1)  # Update COM port as needed
time.sleep(2)  # Wait for connection to establish

def control_appliance(state):
    if state == "ON":
        arduino.write(b'1')  # Send '1' to turn on the appliance
    elif state == "OFF":
        arduino.write(b'0')  # Send '0' to turn off the appliance

# Example usage
if __name__ == "__main__":
    while True:
        command = input("Type ON to turn ON or OFF to turn OFF the appliance: ")
        control_appliance(command.upper())
