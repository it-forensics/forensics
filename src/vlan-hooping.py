#!/usr/bin/python

# This tool is for educational use only!

# Sends a ping packet to another vlan

import sys
from scapy.all import *

def printusage():
  """ Prints usage information """
  print "Usage:   {0} <target_MAC> <target_IP> <src_Vlan> <dst_Vlan".format(sys.argv[0])
  print "  ---> This tool is for educational use only! <---"

if len(sys.argv) < 2:
  printusage()
  sys.exit(1)

packet = Ether(dst=sys.argv[1]) / \
  Dot1Q(vlan=sys.argv[3]) / \
  Dot1Q(vlan=sys.argv[4]) / \
  IP(dst=sys.argv[2]) / \
  ICMP()

# ping to other vlan
sendp(packet)
