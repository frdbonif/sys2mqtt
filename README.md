# **sys2mqtt** v0.2.3

## License

(C) Fred Boniface 2020 <fred@fjla.uk>

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License,  or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

## About

sys2mqtt was born out of my want to view statistics of several systems within OpenHAB.  Using MQTT the data can be displayed or stored in many ways.

sys2mqtt v0.2.3 can publish the folliwing system statistics to an MQTT broker:

- Number of logical CPU Cores
- CPU Utilisation as a percentage
- Total RAM
- RAM utilisation as a percentage
- Total Swap
- Swap utilistation as a percentage

## Compatibility


### v0.2.3 Tested on the following

A newer version is currently available which has been tested on other systems.  The newer version is not yet ready for Windows or FreeBSD.

#### Windows

- Windows 10, Version 2004

#### Other

- FreeBSD, 12.1

## Installation

Firstly, the program requires Python 3 and has been developed using Python 3.8.2.  Please ensure that python3 and the associated pip package is installed on your system.  It relies on the psutil, socket and paho-mqtt Python packages, these can be installed with pip if they are not available on your system.

The current version should be downloaded and placed into a folder of your choosing.  The MQTT URL, port and authentication details should be entered in to the appropriate fields in `conf.py`.  Then you should use either cron or systemd timers to run the `main.py` at your prefererd interval.
