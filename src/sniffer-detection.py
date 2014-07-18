# !/usr/bin/python

# This tool is for educational use only!

# Derscription: Detects if a host in the local area network has sniffs the
# network traffic (runs in promisc mode).

# Requirements: scapy and root privileges

import sys
from scapy.all import promiscping

if len(sys.argv) < 2:
  print "{0} <net>".format(sys.argv[0])
  sys.exit(1)

promiscping(sys.argv[1])
