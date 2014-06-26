#!/usr/bin/python

# This tool is for educational use only!

# Description: Listen on a networkinterface for incomming pings (ICMP packets)
# and display this pings on the console

# Requirements: scapy + root privileges

import sys
from scapy.all import *
from pprint import *

def printusage():
  """ Prints usage information """
  print "Usage:   {0} <iface>".format(sys.argv[0])
  print "  ---> This tool is for educational use only! <---"


if len(sys.argv) < 2:
  printusage()
  sys.exit(1)

def icmp_callback(packet):
  # print the whole networkpacket object on the console
  # TODO: Optimize output...
  pprint(packet)

sniff(prn=icmp_callback, filter="icmp", iface=sys.argv[1], store=0)
