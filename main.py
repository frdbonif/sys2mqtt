#!/usr/bin/env python3

# sys2mqtt version 0.2.2  (C) Fred Boniface 2020
# Distributed under the GPLv3 License

# imports
import socket			    # Included with python3
import random                       # Included with python3
import psutil                       # pip3 install psutil
import paho.mqtt.client as mqtt     # pip3 install paho-mqtt

########## Start of settings block (move to external file) ############

# Set the URL and port of your MQTT broker
# be sure to keep the correct format, as below.
broker_url = "openhab.srv.fjla.uk"
broker_port = 1883

# If your MQTT broker needs authentication
# enter your username and password below.
username = "sys2mqtt"
password = "sys2mqtt"

# Set MQTT QOS Option.  0 = "Send once", 1 = "Broker will receive at least once",
# 2 = "Broker will receive at most once".
q = 1

########################### END OF SETTINGS ###########################

# Get hostname
try:
    host = socket.gethostname()
    print("Host is identified as " + "'" + host + "'")
except:
    print("Unable to identify host,\nusing 'unknown'")
    host = "unknown"


# MQTT parameters
client_rng = random.randrange(0, 99999)
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

getcpu()
getmem()


# Print Topic Paths (DEBUGGING)
#print(corestopic)
#print(cpuutiltopic)
#print(totramtopic)
#print(ramutiltopic)
#print(totswaptopic)
#print(swaputiltopic)

# Initiate MQTT Connection
client = mqtt.Client()
client.username_pw_set(username, password=password)
client.connect(broker_url, broker_port)

# Publish payloads
client.publish(topic=corestopic, payload=cores, qos=q, retain=True)
client.publish(topic=cpuutiltopic, payload=procutil, qos=q, retain=False)
client.publish(topic=totramtopic, payload=totramgbyte, qos=q, retain=True)
client.publish(topic=ramutiltopic, payload=memutil, qos=q, retain=False)
client.publish(topic=totswaptopic, payload=totswapgbyte, qos=q, retain=True)
client.publish(topic=swaputiltopic, payload=swaputil, qos=q, retain=False)
