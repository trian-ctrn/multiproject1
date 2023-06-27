import sys
from Adafruit_IO import MQTTClient
import random as r
import time
import requests

from account import AIO_USERNAME, AIO_KEY

EQUATION_API = "https://io.adafruit.com/api/v2/tinvietle/feeds/equation"
global_equation = ""

def connected(client):
    print("Successfully connected")
    client.subscribe("button1")
    client.subscribe("button2")
    client.subscribe("equation")

def subscribe(client , userdata , mid , granted_qos):
    print("Successfully subscribed")

def disconnected(client):
    print("Disconecting...")
    sys.exit (1)

def message(client , feed_id , payload):
    global global_equation
    print(f"Received payload from \"{feed_id}\": {payload}")
    if (feed_id == "equation"):
        global_equation = payload

def init_global_equation():
    global global_equation
    headers = {}
    x = requests.get(url = EQUATION_API, headers = headers, verify = False)
    data = x.json()
    global_equation = data["last_value"]
    print(f"Latest equation value: {global_equation}")

def calculate(x1, x2, x3):
    result = eval(global_equation)
    print(f"Resut from Adafruit {global_equation}: {result}")
    return result

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

init_global_equation()
client.connect()
client.loop_background()

while True:
    sensor1_value = r.randint(0, 80)
    sensor2_value = r.randint(0, 100)
    sensor3_value = r.randint(0, 10)
    client.publish("sensor1", sensor1_value)
    time.sleep(1)
    client.publish("sensor2", sensor2_value)
    time.sleep(1)
    client.publish("sensor3", sensor3_value)
    time.sleep(1)
    client.publish("plot_result", calculate(sensor1_value, sensor2_value, sensor3_value))
    time.sleep(2)