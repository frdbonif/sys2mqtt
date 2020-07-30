# sys2mqtt version 0.2.3  (C) Fred Boniface 2020
# Distributed under the GPLv3 License

########## Start of settings block (move to external file) ############

# Set the URL and port of your MQTT broker
# be sure to keep the correct format, as below.
broker_url = "mqtt-server"
broker_port = 1883

# If your MQTT broker needs authentication
# enter your username and password below.
username = "mqtt-user"
password = "mqtt-pass"

# Set MQTT QOS Option.  0 = "Send once", 1 = "Broker will receive at least once",
# 2 = "Broker will receive at most once".
q = 1

########################### END OF SETTINGS ###########################
