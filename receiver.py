from config import *
import paho.mqtt.client as mqtt

client = mqtt.Client("receiver")


def on_connect(_client, _userdata, _flags, _rc):
    print("MQTT receiver connected!!")
    client.subscribe(MQTT_TOPIC)


def on_disconnect(_client, _userdata, rc):
    if rc != 0:
        print("Unexpected disconnection of MQTT Broker")
        os.kill(os.getpid(), signal.SIGKILL)


def on_message(_client, _userdata, msg):
    payload = msg.payload.decode("utf-8")
    print("Topic: {}\nPayload: {}\n".format(msg.topic, payload))


if __name__ == "__main__":
    assert client.connect(MQTT_BROKER_ADDR) == 0
    client.on_connect = on_connect
    client.on_message = on_message

    client.on_disconnect = on_disconnect
    client.loop_forever()
