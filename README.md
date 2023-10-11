# RaspberryPi Smart Home Control

<div align="center">
  <img src="https://github.com/Quan20021511/Sel-Navigating-Robot/assets/129273695/aba7195d-7a1e-4769-8541-2ed090ac8a89">
  <img src="https://github.com/Quan20021511/Sel-Navigating-Robot/assets/129273695/401e1173-4727-47ce-b13a-35fe03622387">
</div>

Welcome to the **RaspberryPi Smart Home Control** repository! This project enables you to control various hardware components using a Raspberry Pi. You can interact with devices such as LEDs, motors, a buzzer, and an LCD display through MQTT (Message Queuing Telemetry Transport), allowing for remote control and automation in your smart home.

## Key Features

- **Device Control**: You can remotely control the following hardware components:
  - LEDs
  - Motors
  - Buzzer
  - LCD Display

- **MQTT Communication**: The system uses MQTT for efficient and reliable communication. You can send commands to the Raspberry Pi to control the connected devices.

- **Status Feedback**: An LCD display provides real-time status updates, making it easy to monitor the state of your devices.

## Getting Started

To get started with this project, follow these steps:

1. **Setup Your Raspberry Pi**: Ensure that you have a Raspberry Pi set up and connected to the necessary hardware components.

2. **Install Required Libraries**: Make sure to install the required Python libraries, including `RPi.GPIO` and `paho-mqtt`.

3. **Clone the Repository**: Clone this repository to your Raspberry Pi.

4. **Configure MQTT**: Configure your MQTT broker to allow communication with your Raspberry Pi. You can use a cloud-based broker or set up your own.

5. **Run the Code**: Execute the Python script (`smart_home_control.py`) to start controlling your devices.

## Usage

- Send MQTT messages to control the devices. For example, sending "led_ON" turns on the LED.

- Monitor the status of the devices on the LCD display.

- Extend the functionality by adding more devices or customizing the code to fit your specific needs.

## Contributing

If you're interested in contributing to this project, feel free to submit pull requests or open issues. We welcome improvements, bug fixes, and additional features.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to the open-source community for the libraries and tools that made this project possible.

Happy hacking and enjoy your smart home control system! 🏡🚀
