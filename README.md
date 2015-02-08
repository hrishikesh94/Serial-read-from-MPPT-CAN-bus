# Serial-read-from-MPPT-CAN-bus
A program that decodes the CAN bus data received from MPPT in the  IEEE single-precision 32-bit format (IEEE 754). This data is then transmitted over a serial line via xbee to ground station. This was built to be used in the university Solar Car project

#Serialconnectioncheck.py
this file is used to initialize the ewart candapter, open the port and receive the data from the MPPT canbus.


