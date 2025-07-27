FROM kalilinux/kali-rolling:latest

# Install OSINT and social engineering tools
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    python3-pip \
    git \
    curl \
    wget \
    exiftool \
    whois \
    dnsutils \
    nmap \
    nikto \
    dirb \
    gobuster \
    theharvester \
    recon-ng \
    spiderfoot \
    maltego \
    set \
    fierce \
    metagoofil \
    && rm -rf /var/lib/apt/lists/*

# Install Python-based OSINT tools
RUN pip3 install \
    socialscan \
    holehe \
    sherlock-project \
    phoneinfoga \
    maigret \
    twint \
    instagram-scraper \
    linkedin-scraper

# Clone additional tools
RUN git clone https://github.com/Datalux/Osintgram.git /opt/osintgram && \
    git clone https://github.com/laramies/theHarvester.git /opt/theHarvester && \
    git clone https://github.com/smicallef/spiderfoot.git /opt/spiderfoot

# Copy custom scripts
COPY scripts/ /scripts/
RUN chmod +x /scripts/*.sh /scripts/*.py

# Create working directories
RUN mkdir -p /data/osint /data/profiles /data/campaigns

WORKDIR /data

# Set up aliases
RUN echo "alias ll='ls -la'" >> /root/.bashrc && \
    echo "alias profile-gen='python3 /scripts/profile_generator.py'" >> /root/.bashrc && \
    echo "alias wiki-gen='python3 /scripts/wikipedia_generator.py'" >> /root/.bashrc

CMD ["/bin/bash"]