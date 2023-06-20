from Adafruit_IO import MQTTClient
import random
import time
from account import AIO_USERNAME, AIO_KEY

AIO_FEED_ID = "sensor1"

def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe(AIO_FEED_ID)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)
    
    
if __name__ == '__main__':
    client = MQTTClient(AIO_USERNAME, AIO_KEY)
    client.on_connect = connected
    client.on_disconnect = disconnected
    client.on_message = message
    client.on_subscribe = subscribe
    client.connect()
    client.loop_background()
    while True:
        value = 30 + random.randint(-10, 10)
        client.publish(AIO_FEED_ID, value)
        time.sleep(5)
