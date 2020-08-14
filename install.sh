#!/bin/bash

echo "sys2mqtt v0.4.0"
echo "sys2mqtt will now be installed as a systemd service, if you do not use systemd this script will not work on your system"
echo "This script will currently only install on Debian, Ubuntu & Raspberry Pi OS systems"
echo "Would you like to continue? (y/n)"
read var_cont

if [ $var_cont = n ]
then
 echo "You have chosen not to continue."
 echo "Visit https://sys2mqtt.fjla.uk for alternative installation methods"
 exit 1

elif [ $var_cont = y ]
then
 chmod -R 0755 python
 apt install python3 python3-pip -y
 pip3 install psutil paho-mqtt distro
 cp systemd/sys2mqtt-deb.service /etc/systemd/system/sys2mqtt.service
 systemctl daemon-reload
 systemctl enable sys2mqtt.service
 systemctl start sys2mqtt.service
 exit 0
else
 echo "That isn't a valid choice, try starting the script again or checking out the sys2mqtt readme."
 exit 2
fi
exit
