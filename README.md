# Pi-Heartbeat-broadcast
Python script to send heartbeat from raspberry pi 

This project provides a Python script for a Raspberry Pi to send heartbeat signals via I2C to an ATtiny85 microcontroller. The heartbeat signals are sent periodically to ensure the ATtiny85 remains active and powers on the servo rail. If the heartbeat signals stop, the ATtiny85 will power down the servo rail for safety.

## Features

- Sends heartbeat signals ('H') via I2C to the ATtiny85.
- Configurable heartbeat interval.
- Automatically starts on boot using a systemd service.

## Hardware Requirements

- Raspberry Pi with I2C enabled
- ATtiny85 microcontroller
- Servo rail
- Supporting electronic components (e.g., resistors, capacitors)
- I2C connections between Raspberry Pi and ATtiny85

## Dependencies

- Python 3
- smbus library
- i2c-tools

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Pi-Heartbeat-Sender.git
    ```

2. Navigate to the project directory:
    ```sh
    cd Pi-Heartbeat-Sender
    ```

3. Install the required Python package:
    ```sh
    sudo apt-get update
    sudo apt-get install -y python3-smbus i2c-tools
    ```

## Enabling I2C on the Raspberry Pi

1. Enable I2C by editing the boot configuration:
    ```sh
    sudo nano /boot/firmware/config.txt
    ```
    Add the following line:
    ```txt
    dtparam=i2c_arm=on
    ```

2. Reboot the Raspberry Pi to apply changes:
    ```sh
    sudo reboot
    ```

3. Verify the I2C bus:
    ```sh
    ls /dev/i2c-*
    ```

## Usage

1. Ensure your hardware is connected correctly:
    - Raspberry Pi SDA (GPIO 2) to ATtiny85 SDA (pin 5)
    - Raspberry Pi SCL (GPIO 3) to ATtiny85 SCL (pin 7)
    - Common Ground between Raspberry Pi and ATtiny85

2. Run the Python script manually to test:
    ```sh
    python3 send_heartbeat.py
    ```

3. To run the script automatically at boot, create a systemd service:

    - Create a new service file:
        ```sh
        sudo nano /etc/systemd/system/heartbeat.service
        ```

    - Add the following content:
        ```ini
        [Unit]
        Description=Heartbeat Service
        After=multi-user.target

        [Service]
        ExecStart=/usr/bin/python3 /home/pi/Pi-Heartbeat-Sender/send_heartbeat.py
        Restart=always
        User=pi

        [Install]
        WantedBy=multi-user.target
        ```

    - Enable and start the service:
        ```sh
        sudo systemctl enable heartbeat.service
        sudo systemctl start heartbeat.service
        ```

    - Check the status of the service:
        ```sh
        sudo systemctl status heartbeat.service
        ```

## Python Script

```python
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
```

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

### Contact

Author: Farhang Naderi

Email: farhang.naderi@uri.edu
