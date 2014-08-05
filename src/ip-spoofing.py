#!/usr/bin/python

# This tool is for educational use only!

# Description: Sends a ping (ICMP) packet with a wrong source IP (The
# source IP does not match the source MAC address in the LAN). Scapy automaticly
# sets the clients MAC address if the layer 2 is not assembled manualy.

# Requirements: scapy + root privileges

import sys
import pprint
from scapy.all import send, IP, ICMP

if len(sys.argv) < 3:
  print "{0} <srv_ip> <dst_ip>".format(sys.argv[0])
  sys.exit(1)

# Assemble a icmp packet with the given source and destination IP's and send it
send(IP(src=sys.argv[1], dst=sys.argv[2]) / ICMP())
