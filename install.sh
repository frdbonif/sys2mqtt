#!/bin/sh

echo "Installer script for sys2mqtt v0.2.9"
echo ""
echo "Copying and enabling sys2mqtt service"

cp sys2mqtt.service  /etc/systemd/system/sys2mqtt.service

systemctl daemon-reload
systemctl enable sys2mqtt.service
systemctl start sys2mqtt.service

echo ""
echo "Service has now been enabled and started"
echo "To change configuration, issue 'systemctl stop sys2mqtt' before editing"
echo "the conf.py file."
