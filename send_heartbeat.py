"""
Pi-Heartbeat-Sender

Author: Farhang Naderi
Email: farhang.naderi@uri.edu
License: MIT License
Year: 2024

Description:
This Python script runs on a Raspberry Pi to send heartbeat signals via I2C to an ATtiny85 microcontroller.
The heartbeat signals are sent periodically to ensure the ATtiny85 remains active and powers on the servo rail.
If the heartbeat signals stop, the ATtiny85 will power down the servo rail for safety.
"""

import smbus
import time

# Initialize I2C (SMBus)
bus = smbus.SMBus(1)  # Use I2C bus 1

# I2C address of the ATtiny85
ATTINY85_I2C_ADDRESS = 0x08

# Heartbeat character to send
HEARTBEAT = ord('H')

def send_heartbeat():
    try:
        # Send heartbeat signal to ATtiny85
        bus.write_byte(ATTINY85_I2C_ADDRESS, HEARTBEAT)
        print("Heartbeat sent")
    except Exception as e:
        print(f"Error sending heartbeat: {e}")

if __name__ == "__main__":
    while True:
        send_heartbeat()
        time.sleep(1)  # Wait for 1 second before sending the next heartbeat
