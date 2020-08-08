#!/usr/bin/env python3

# sys2mqtt version 0.4.0  (C) Fred Boniface 2020
# Distributed under the GPLv3 License

# imports
from socket import gethostname      # Included with python3
from random import randrange        # Included with python3
from time import sleep              # Included with python3
from os import name as platname     # Included with python3  >>?
import platform                     # Included with python3  >>?
import atexit                       # Included with python3
import conf                         # Included with sys2mqtt
import distro                       # pip3 install distro
import psutil                       # pip3 install psutil
import paho.mqtt.client as mqtt     # pip3 install paho-mqtt

# Get hostname
try:
    host = gethostname()
    print("Host is identified as " + "'" + host + "'")
except:
    print("Unable to identify host,\nusing 'unknown'")
    host = "unknown"

# Get platform
try:
    platform_type = platname
    if(platform_type == 'posix'):
        platform_dic = distro.linux_distribution()
        op_sys = (platform_dic[0])
        op_sys_ver = (platform_dic[1])
        print(op_sys + " " + op_sys_ver + " detected")
    elif(platform_type == 'nt'):
        platform_dic = platform.uname()
        op_sys = (platform_dic[0])
        op_sys_ver = (platform_dic[1])
        print(op_sys + " " + op_sys_ver + " detected")
    elif(platform_type == 'java'):
        op_sys = 'Java VM'
        op_sys_ver = 'Version Unknown'
        print(op_sys + " " + op_sys_ver + " detected")
    else:
        op_sys = 'Unknown'
        op_sys_ver = 'Unknown'
except:
    platform_type = 'Unknown'

#DEBUG-BLOCK
print(platform_type)
print(op_sys)
print(op_sys_ver)
#END-DEBUG-BLOCK

## This generates a random Client ID to prevent clashes on the MQTT broker ##
client_rng = randrange(0, 99999)
client_id = "sys2mqtt_{}".format(client_rng)

## MQTT Topics ##
## These are the default MQTT topics used by sys2mqtt ##
mqos = "sys2mqtt/" + host + "/sys/os"
mqosver = "sys2mqtt/" + host + "/sys/os/ver"
mqlogcores = "sys2mqtt/" + host + "/cpu/cores"
mqcpuutil = "sys2mqtt/" + host + "/cpu/util"
mqtotram = "sys2mqtt/" + host + "/mem/ram/total"
mqramutil = "sys2mqtt/" + host + "/mem/ram/util"
mqtotswap = "sys2mqtt/" + host + "/mem/swap/total"
mqswaputil = "sys2mqtt/" + host + "/mem/swap/util"
mqconnect = "sys2mqtt/" + host + "/sys/connect"
mqupdate = "sys2mqtt/" + host + "sys/lastupdate"

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

# Gather MQTT Broker information and initiate connection
client = mqtt.Client()
client.username_pw_set(conf.username, password=conf.password)
client.connect(conf.broker_url, conf.broker_port)
client.publish(topic=mqconnect, payload='Yes', qos=conf.q, retain=False)

# Define what to do if program is exited.
def exiting():
    print("Program exiting")
    client.publish(topic=mqcpuutil, payload=0, qos=conf.q, retain=False)
    client.publish(topic=mqramutil, payload=0, qos=conf.q, retain=False)
    client.publish(topic=mqswaputil, payload=0, qos=conf.q, retain=False)
    client.publish(topic=mqconnect, payload='No', qos=conf.q, retain=False)

# Register exit action so it will be executed if program exits.
atexit.register(exiting)

# Publish static metrics once per startup.
client.publish(topic=mqos, payload=op_sys, qos=conf.q, retain=True)
client.publish(topic=mqosver, payload=op_sys_ver, qos=conf.q, retain=True)
client.publish(topic=mqlogcores, payload=cores, qos=conf.q, retain=True)
client.publish(topic=mqtotram, payload=totramgbyte, qos=conf.q, retain=True)
client.publish(topic=mqtotswap, payload=totswapgbyte, qos=conf.q, retain=True)

while True:

  getcpu()
  getmem()
  print("Loop Completed")
    
  # Publish dynamic payloads
  client.publish(topic=mqcpuutil, payload=procutil, qos=conf.q, retain=False)
  client.publish(topic=mqramutil, payload=memutil, qos=conf.q, retain=False)
  client.publish(topic=mqswaputil, payload=swaputil, qos=conf.q, retain=False)

  sleep(10)
