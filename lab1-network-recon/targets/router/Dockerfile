FROM ubuntu:20.04

# Install services commonly found on routers
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    telnetd \
    xinetd \
    openssh-server \
    apache2 \
    snmpd \
    net-tools \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

# Configure telnet (intentionally insecure)
RUN echo "telnet stream tcp nowait telnetd /usr/sbin/tcpd /usr/sbin/in.telnetd" > /etc/inetd.conf

# Create weak admin account
RUN useradd -m -s /bin/bash admin && \
    echo "admin:admin" | chpasswd

# Configure SSH to allow password authentication
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Setup router web interface
COPY router-web /var/www/html/

# Configure SNMP with default community string
RUN echo "rocommunity public" > /etc/snmp/snmpd.conf && \
    echo "syslocation Ron's Coffee Shop Router" >> /etc/snmp/snmpd.conf && \
    echo "syscontact admin@ronscoffee.com" >> /etc/snmp/snmpd.conf

# Startup script
COPY startup.sh /startup.sh
RUN chmod +x /startup.sh

EXPOSE 23 22 80 161/udp

CMD ["/startup.sh"]