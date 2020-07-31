# **sys2mqtt** v0.2.9

## License

(C) Fred Boniface 2020 <fred@fjla.uk>

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License,  or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

## About

sys2mqtt was born out of my want to view statistics of several systems within OpenHAB.  Using MQTT the data can be displayed or stored in many ways.

sys2mqtt v0.2.9 can publish the folliwing system statistics to an MQTT broker:

- Number of logical CPU Cores
- CPU Utilisation as a percentage
- Total RAM
- RAM utilisation as a percentage
- Total Swap
- Swap utilistation as a percentage

## Compatibility

The program has been tested for compatibility on the following operating systems, for further compatibility information you can check the documentation for psutil on GitHub.

### v0.2.9 will not be Tested until v0.3.0 --on the following--

It is likely that sys2mqtt will run on a number of systems but cannot be tested on every distro.
All non-Windows systems listed below have been tested using default repos unless otherwise noted.
See footnotes for notes.

#### Linux

- CentOS 8
- Debian 10
- Sangoma Linux 7.6
- Ubuntu, 18.04, 20.04

#### Windows

- Windows 10, Version 2004

#### Other

- FreeBSD, 12.1

## Installation

Firstly, the program requires Python 3 and has been developed using Python 3.8.2.  Please ensure that python3 and the associated pip package is installed on your system.  It relies on the psutil, socket and paho-mqtt Python packages, these can be installed with pip if they are not available on your system.

You can install sys2mqtt as follows on Debian based systems, for other systems consult the wiki.  (Commands starting $ to be run as user, commands starting # to be run as root or using sudo)

Ensure dependencies are available.
`#``apt install python3 python3-pip`

Move to the correct directory for installing.
`$``cd /usr/local/bin`

Clone the source of sys2mqtt.
`#``git clone https://github.com/frdbonif/sys2mqtt.git`

Move in to the newly created directory.
`$``cd sys2mqtt`

Make sure the installer script is executable.
`#``chmod +x install.sh`

Run the installer script.  Be aware: You should always check scripts before you run them to be sure you know what they are modifying on your system.  If you'd rather not run the installer script, check the wiki for alternative methods.
`#``./install.sh`

## MQTT Topics

This information will be available on the sys2mqtt wiki.

## Task List

- [X] 0.2.2 Provide QoS Option for MQTT.
- [X] 0.2.3 Create sys2mqtt as Python package.
- [X] 0.2.3 Move user selectable optiond from `main.py` to `conf.py`.
- [X] 0.2.3 Test in Debian.
- [X] 0.2.4 Create and include systemd service file.
- [X] 0.3.0 Change name of `main.py` to `sys2mqtt.py`
- [ ] 0.3.0 Create installer script.
- [ ] 0.3.0 Insert loop into program to remove reliance on cron or systemd timers.
- [ ] 0.3.1 Inclusion of drive information.
- [ ] 0.3.1 Implement ON/OFF state setting suitable parameters to zero on shutdown.
- [ ] 0.3.2 Inclusion of temerature and fan information.
- [ ] 0.4.0 Extend `conf.py` file to allow users to choose which metrics they would like enabled.
- [ ] 0.5.0 Improved error handling.
- [ ] 0.5.1 Move to self hosted git solution.
- [ ] 0.5.2 Create wiki for documentation.
- [ ] 0.9.9(rc) Logging.

## Footnotes

Only tested on Intel CPU's although believed to work on other x86 CPU's.

### For Sangoma Linux 7.6 ensure to install the following first:

- pip `yum install python36u-pip`
- python3 devel `yum install python36u-devel`

Once these packages have been installed from the default repos you can continue to install the python package dependencies using pip3.6.

The script should be invoked using `python3.6 /usr/local/bin/sys2mqtt/sys2mqtt.py`.
