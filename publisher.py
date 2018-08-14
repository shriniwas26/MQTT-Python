from config import *
from time import sleep
import paho.mqtt.client as mqtt
import os, signal
client = mqtt.Client("receiver")


def on_publish(_client, _userdata, result):  # create function for callback
    print("Message number: " + str(result))


def on_disconnect(_client, _userdata, _result):
    print("Disconnected, killing app")
    os.kill(os.getpid(), signal.SIGKILL)


def on_connect(_client, _userdata, _flags, _result):
    print("Publisher connected")


if __name__ == "__main__":
    client = mqtt.Client("broadcaster")
    client.on_publish = on_publish
    client.on_disconnect = on_disconnect
    client.on_connect = on_connect
    assert client.connect(MQTT_BROKER_ADDR) == 0
    client.loop_start()
    i = 0
    while True:
        i += 1
        client.publish(MQTT_TOPIC, "Hello", qos=1)
        sleep(1)
