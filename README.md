# **sys2mqtt** v0.4.0

## License

(C) Fred Boniface 2020 <fred@fjla.uk>

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License,  or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

## About

sys2mqtt was born out of my want to view statistics of several systems within OpenHAB.  Using MQTT the data can be displayed or stored in many ways.

sys2mqtt v0.4.0 can publish the folliwing system statistics to an MQTT broker:

- OS Name and version
- Number of logical CPU Cores
- CPU Utilisation as a percentage
- Total RAM
- RAM utilisation as a percentage
- Total Swap
- Swap utilistation as a percentage

## Compatibility

The program has been tested for compatibility on the following operating systems, for further compatibility information you can check the documentation for psutil on GitHub.

### v0.3.0 Tested on: ***v0.4.0 requires full testing before merging to master***

It is likely that sys2mqtt will run on a number other of systems but cannot be tested on every distro.
All non-Windows systems listed below have been tested using default repos unless otherwise noted.
See footnotes for notes.

#### Linux

- CentOS 8
- Debian 10
- Sangoma Linux 7.6<sup> 1</sup>
- Ubuntu, 18.04, 20.04
- Rasperry Pi OS/Rasbian, 10<sup> 2</sup>

#### Windows

- Windows 10, Version 2004

#### Other

- FreeBSD 12 (No installation intructions)

#### Known not working

- Jython, this project uses modules that are not available to Jython.
- Python 2.x, this project is not compatible with Python 2.x which is no longer supported.  Python 2.x and Python 3.x can run independently on the same device if needed.

## Installation 

Installation instructions for various operating systems/platforms.  Once we have a working wiki this will be moved there but for now, I'll leave it to clutter up the README.

If you want to use sys2mqtt on another system that isn't listed, it's very likely to work as a cross-platform approach was taken when choosing which packages to import and when writing the code.  As long as your chosen platform can run `python3` and can run the program at boot then you should be fine.  If you get it working then please do share, you can even update the install guides to help others.

### Install with `install.sh` (Debian & Ubuntu)

See the bottom of the page for installation on other systems, we don't have a wiki at the moment.

Firstly, the program requires Python 3 and has been developed using Python 3.8.2.  It also relies on the psutil, socket and paho-mqtt Python packages.  If you follow the method below, these will all be installed for you.

You can install sys2mqtt as follows on Debian based systems.  (Commands starting $ to be run as user, commands starting # to be run as root or using sudo)

Ensure dependencies are available.
`#``apt install git`

Move to the correct directory for installing.
`$``cd /usr/local/bin`

Clone the source of sys2mqtt.
`#``git clone https://github.com/frdbonif/sys2mqtt.git`

Move in to the newly created directory.
`$``cd sys2mqtt`

Make sure the required files are executable.
`#``chmod +x install.sh`

Run the installer script.  Be aware: You should always check scripts before you run them to be sure you know what they are modifying on your system.  If you'd rather not run the installer script, check the bottom of this README for alternative options.
`#``./install.sh`

### Install on Sangoma Linux 7.6 (login as root)

- `yum install python36u-pip python36u-devel git`
- `pip install psutil paho-mqtt`
- `cd /usr/local/bin`
- `git clone https://github.com/frdbonif/sys2mqtt.git`
- `cd sys2mqtt`

Now, open the python/conf.py file and enter the details for your MQTT server.

- `cd /usr/local/bin/sys2mqtt`
- `chmod -R 0755 python`
- `cp systemd/sys2mqtt-sangoma76.service /etc/systemd/system/sys2mqtt.service`
- `systemctl daemon-reload`
- `systemctl enable sys2mqtt.service`
- `systemctl start sys2mqtt.service`

### Install on CentOS 8 (login as root)

- `yum install python3 python3-pip git`
- `pip3 install psutil paho-mqtt --user`
- `cd /usr/local/bin`
- `git clone https://github.com/frdbonif/sys2mqtt.git`
- `cd sys2mqtt`

Now, open the python/conf.py file and enter the details for your MQTT server.

- `cd /usr/local/bin/sys2mqtt`
- `chmod -R 0755 python`
- `cp systemd/sys2mqtt.service /etc/systemd/system/sys2mqtt.service`
- `systemctl daemon-reload`
- `systemctl enable sys2mqtt.service`
- `systemctl start sys2mqtt.service`

### Install on FreeBSD

FreeBSD users should use the v0.2.3 branch until running sys2mqtt as a service on FreeBSD has been implemented.  This branch can be downloaded with the command: `git clone -b v0.2.3 https://github.com/frdbonif/sys2mqtt.git

### Install on Windows

- To install v0.4.0 on Windows, download the .zip from GitHub (Click on the 'Code' button at the top right of the page).
- Extract the .zip file into `C:\sys2mqtt\`
- Open `Task Scheduler`, you will need to run this as an Administrator.
- Create a new custom task that runs `sys2mqtt` at boot as the `system` user.
    - To run sys2mqtt, choose the program location `C:\sys2mqtt\python\sys2mqtt.py`

## Footnotes

- <sup>1 </sup> Tested on FreePBX Install.
- <sup>2 </sup> Tested on Rasbian 10 on Raspberry Pi 3B.
