# sys2mqtt version 0.4.0  (C) Fred Boniface 2020
# Distributed under the GPLv3 License

import yaml

# Open and parse conf.yaml

try:
    with open('/etc/sys2mqtt/conf.yaml') as cnf:
        yamlConf = yaml.load(cnf, Loader=yaml.FullLoader)
    print("Loaded configuration from '/etc/sys2mqtt/conf.yaml'")
except (FileNotFoundError):
    with open('conf.yaml') as cnf:
        yamlConf = yaml.load(cnf, Loader=yaml.FullLoader)
    print("Loaded configuration from 'prog' folder")

# Create separate dictionaries for each 'section'
mqttConf = yamlConf.get('mqtt conf')
testConf = yamlConf.get('test-conf')

# Create variables for each individual option.
broker = mqttConf.get('broker')
port = mqttConf.get('port')
user = mqttConf.get('username')
passwd = mqttConf.get('password')
qos = mqttConf.get('qos')
baseTopic = mqttConf.get('baseTopic')
discovery = mqttConf.get('discovery')
