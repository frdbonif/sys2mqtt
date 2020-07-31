#!/usr/bin/env python3

# sys2mqtt version 0.2.9  (C) Fred Boniface 2020
# Distributed under the GPLv3 License

# imports
from socket import gethostname      # Included with python3
from random import randrange        # Included with python3
import psutil                       # pip3 install psutil
import paho.mqtt.client as mqtt     # pip3 install paho-mqtt
import conf                         # Included with sys2mqtt
from time import sleep              # Included with python3

# Get hostname
try:
    host = gethostname()
    print("Host is identified as " + "'" + host + "'")
except:
    print("Unable to identify host,\nusing 'unknown'")
    host = "unknown"


# MQTT parameters
client_rng = randrange(0, 99999)
client_id = "sys2mqtt_{}".format(client_rng)
# Topics
corestopic = "sys2mqtt/" + host + "/cpu/cores"
cpuutiltopic = "sys2mqtt/" + host + "/cpu/util"
totramtopic = "sys2mqtt/" + host + "/mem/ram/total"
ramutiltopic = "sys2mqtt/" + host + "/mem/ram/util"
totswaptopic = "sys2mqtt/" + host + "/mem/swap/total"
swaputiltopic = "sys2mqtt/" + host + "/mem/swap/util"

# Get static metrics - CPU Cores, Total RAM, Total SWAP.
cores = psutil.cpu_count() # Get cores
print("{} cores identified".format(cores))
virtmem = psutil.virtual_memory() # Get RAM details
totrambyte = virtmem[0] # Get total RAM
totramgbyte = round(totrambyte / 1073741824, 1) # Convert to GB (1 decimal place)
print("Total RAM = {} GB".format(totramgbyte))
swapmem = psutil.swap_memory() # Get swap details
totswapbyte = swapmem[0] # Get total swap
totswapgbyte = round(totswapbyte / 1073741824, 1) # Convert to GB (1 decimal place)
print("Total swap = {} GB".format(totswapgbyte))

# Get CPU Cores & Utilisation
def getcpu():
    global procutil

    procutil = psutil.cpu_percent() # Get CPU usage
    print("CPU utilisation = {}%".format(procutil))

# Get RAM Utilisation
def getmem():
    global virtmem, memutil, swapmem, swaputil

    memutil = virtmem[2] # Get RAM util
    print("RAM utilisation = {}%".format(memutil))
    swaputil = swapmem[3] # Get swap util
    print("Swap utilisation = {}%".format(swaputil))


  # Initiate MQTT Connection

# Gather MQTT Broker information and initiate connection
client = mqtt.Client()
client.username_pw_set(conf.username, password=conf.password)
client.connect(conf.broker_url, conf.broker_port)

# Publish static metrics once per startup.
client.publish(topic=corestopic, payload=cores, qos=conf.q, retain=True)
client.publish(topic=totramtopic, payload=totramgbyte, qos=conf.q, retain=True)
client.publish(topic=totswaptopic, payload=totswapgbyte, qos=conf.q, retain=True)

while True:

  getcpu()
  getmem()
  print("Loop Completed")
    
  # Publish dynamic payloads
  client.publish(topic=cpuutiltopic, payload=procutil, qos=conf.q, retain=False)
  client.publish(topic=totramtopic, payload=totramgbyte, qos=conf.q, retain=True)
  client.publish(topic=ramutiltopic, payload=memutil, qos=conf.q, retain=False)
  client.publish(topic=totswaptopic, payload=totswapgbyte, qos=conf.q, retain=True)
  client.publish(topic=swaputiltopic, payload=swaputil, qos=conf.q, retain=False)

  sleep(10)
