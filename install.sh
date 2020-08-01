 #!/bin/bash

 echo "sys2mqtt v0.3.0"
 echo "sys2mqtt will now be installed as a systemd service, if you do not use systemd this script will not work"
 echo "This script will currently only install on Debian and Ubuntu systems"
 echo "Would you like to continue? (y/n)"
 read var_cont

 if [ $var_cont = n ]
 then
    echo "You have chosen not to continue."
    echo "Visit the sys2mqtt readme for alternative installation methods"
    exit 1
    
 elif [ $var_cont = y ]
 then
    echo "sys2mqtt is now installing..."
    chmod -R 0755 python
    echo "Installing apt dependencies..."
    apt install python3 python3-pip -y
    echo "Installing pip dependencies..."
    pip3 install psutil paho-mqtt
    echo "Installing and enabling sys2mqtt service..."
    cp systemd/sys2mqtt.service /etc/systemd/system/sys2mqtt.service
    systemctl daemon-reload
    systemctl enable sys2mqtt.service
    echo "Starting sys2mqtt..."
    systemctl start sys2mqtt.service
    echo "sys2mqtt has been installed and started.  It will automatically start after every reboot."
    exit 0
else
    echo "That isn't a valid choice, try starting the script again or checking out the sys2mqtt readme."
    exit 2
fi
exit
