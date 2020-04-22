import paho.mqtt.client as paho
import json
import time
import random
import sys

broker="localhost"
port=1883

initial_temperature = random.random()*20
initial_humidity = random.random()*100

def on_publish(client,userdata,result):         #create function for callback
    print("data published \n")
    pass

client1= paho.Client()                           #create client object
client1.on_publish = on_publish              #assign function to callback

while True:
  client1.connect(broker,port)              #establish connection
  temperature = initial_temperature + (0.5-random.random())
  humidity = initial_humidity + (0.5-random.random())
  data = {"id":sys.argv[1],"temperatura":temperature,"humedad":humidity}
  ret= client1.publish("casa/sensor1/readings",json.dumps(data))
  time.sleep(10)
