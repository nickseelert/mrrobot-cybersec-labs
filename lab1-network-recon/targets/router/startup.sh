#!/bin/bash

# Start SSH service
service ssh start

# Start Apache
service apache2 start

# Start SNMP
service snmpd start

# Start telnet
service xinetd start

# Keep container running
tail -f /dev/null