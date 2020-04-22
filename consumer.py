import paho.mqtt.client as mqtt
import json


def on_connect(client, userdata, flags, rc):
	print("Connected with result code:"+str(rc))
	client.subscribe("casa/+/readings")

def on_message(client, data, msg):
    print("Topic:"+msg.topic)
    print("Message:"+msg.payload)
    message = json.loads(msg.payload)
    print("Message:"+str(message))
		
		
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost",1883,60)
print("Conecting with brocker")

client.loop_forever()
