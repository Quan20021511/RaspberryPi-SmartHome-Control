#!/usr/bin/python
import time
import os
from urllib.parse import urlparse
import RPi.GPIO as GPIO
import paho.mqtt.client as paho

# Constants for LCD
LCD_WIDTH = 16
LCD_CMD = False
LCD_CHR = True
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0
LCD_LINE_3 = 0x90
LCD_LINE_4 = 0xD0
E_PULSE = 0.0005
E_DELAY = 0.0005

# Define GPIO pins
LCD_RS = 7
LCD_E = 11
LCD_D4 = 12
LCD_D5 = 13
LCD_D6 = 15
LCD_D7 = 16
bulb_pin = 29
dc_motor1 = 31
dc_motor2 = 32
led_pin = 33
buzzer_pin = 36

# Set GPIO mode and warnings
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Initialize GPIO pins
pins = [LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7, bulb_pin, dc_motor1, dc_motor2, led_pin, buzzer_pin]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

# MQTT callbacks
def on_connect(client, userdata, flags, rc):
    client.subscribe("led", 0)

def on_message(client, userdata, msg):
    message = msg.payload
    if message == b"led_ON":
        update_display("LED ON", LCD_LINE_1)
        GPIO.output(led_pin, GPIO.HIGH)
    elif message == b"led_OFF":
        update_display("LED OFF", LCD_LINE_1)
        GPIO.output(led_pin, GPIO.LOW)
    # Add similar blocks for other MQTT messages

def on_publish(client, userdata, mid):
    print("mid: " + str(mid))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# MQTT client setup
mqttc = paho.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Connect to MQTT broker
url_str = os.environ.get('CLOUDMQTT_URL', 'tcp://broker.emqx.io:1883')
url = urlparse(url_str)
mqttc.connect(url.hostname, url.port)

# LCD initialization
def lcd_init():
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)
    time.sleep(E_DELAY)

# Function for sending data to LCD
def lcd_byte(bits, mode):
    GPIO.output(LCD_RS, mode)
    GPIO.output(LCD_D4, bits & 0x10 == 0x10)
    GPIO.output(LCD_D5, bits & 0x20 == 0x20)
    GPIO.output(LCD_D6, bits & 0x40 == 0x40)
    GPIO.output(LCD_D7, bits & 0x80 == 0x80)
    lcd_toggle_enable()
    GPIO.output(LCD_D4, bits & 0x01 == 0x01)
    GPIO.output(LCD_D5, bits & 0x02 == 0x02)
    GPIO.output(LCD_D6, bits & 0x04 == 0x04)
    GPIO.output(LCD_D7, bits & 0x08 == 0x08)
    lcd_toggle_enable()

# Function for toggling Enable pin
def lcd_toggle_enable():
    time.sleep(E_DELAY)
    GPIO.output(LCD_E, True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)
    time.sleep(E_DELAY)

# Function for updating the LCD display
def update_display(message, line):
    message = message.ljust(LCD_WIDTH, " ")
    lcd_byte(line, LCD_CMD)
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

# LCD initialization
lcd_init()
update_display("Welcome", LCD_LINE_1)
time.sleep(0.5)
update_display("LED OFF", LCD_LINE_1)
update_display("Bulb OFF", LCD_LINE_2)
update_display("Motor Stop", LCD_LINE_3)
update_display("Buzzer OFF", LCD_LINE_4)

# Main loop
while True:
    rc = mqttc.loop()
    time.sleep(0.5)
