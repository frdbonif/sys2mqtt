# **sys2mqtt** v0.2.2

## License

(C) Fred Boniface 2020 <fred@fjla.uk>

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License,  or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

## About

sys2mqtt was born out of my want to view statistics of several systems within OpenHAB.  Using MQTT the data can be displayed or stored in many ways.

sys2mqtt v0.2.2 can publish the folliwing system statistics to an MQTT broker:

- Number of logical CPU Cores
- CPU Utilisation as a percentage
- Total RAM
- RAM utilisation as a percentage
- Total Swap
- Swap utilistation as a percentage

## Compatibility

The program has been tested for compatibility on the following operating systems, for further compatibility information you can check the documentation for psutil on GitHub.

### v0.2.2 Tested on the following

For details of previous versions tested and compatibility with other platforms see the wiki.
See footnotes for notes.

#### Linux

- Ubuntu, 18.04^1^, 20.04^1^
- CentOS, 8^1^

#### Windows

- Windows 10, Version 2004^1^

#### Other

- FreeBSD, 12.1^1

#### Currently known not working

- Sangoma Linux 7 (paho-mqtt does not run)

## Installation

Firstly, the program requires Python 3 and has been developed using Python 3.8.2.  Please ensure that python3 and the associated pip package.  It relies on the psutil, socket and paho-mqtt Python packages, these can be installed with pip if they are not available on your system.

The current version should be downloaded and placed into a folder of your choosing.  The MQTT URL, port and authentication details should be entered in to the appropriate fields in `main.py`.  Then you should use either cron or systemd timers to run the program at your prefererd interval.  For further information see the sys2mqtt wiki.

## MQTT Topics

This information will be available on the sys2mqtt wiki.

## Task List

- [X] 0.1.0 Test v0.1 on Windows 10.
- [X] 0.2.0 Add Windows 10 hostname resolution support.
- [X] 0.2.0 Add copyright and lisence details to `main.py` and `conf.py`.
- [X] 0.2.2 Move totalram and totalswap checks out from function to main body, repetetive checking of static metrics is wasteful.
- [X] 0.2.2 Test on FreeBSD.
- [X] 0.2.2 Test on CentOS.
- [ ] 0.2.2 Test on Debian.
- [X] 0.2.2 Test on Sangoma Linux 7 (CentOS 7 Based).  Likely common with CentOS 7 which is EOL.
- [ ] 0.2.2 Provide QoS Option for MQTT.
- [ ] 0.2.3 Create sys2mqtt as Python package.
- [ ] 0.2.3 Move user selectable optiond from `main.py` to `conf.py`.
- [ ] 0.2.3 Implement ON/OFF state setting suitable parameters to zero on shutdown.
- [ ] 0.2.4 Create and include systemd service file.
- [ ] 0.3.0 Insert loop into program to remove reliance on cron or systemd timers.
- [ ] 0.3.1 Inclusion of drive information.
- [ ] 0.4.0 Inclusion of temerature and fan information.
- [ ] 0.5.0 Extend `conf.py` file to allow users to choose which metrics they would like enabled.
- [ ] 0.5.1 Improved error handling.
- [ ] 0.5.1 Move to self hosted git solution.
- [ ] 0.5.2 Create wiki for documentation.
- [ ] 1.0.0 Logging.

## Footnotes

^1 Only tested with Intel 64-bit processors, there is no known reasons for it not to work with 32-bit or AMD processors.
