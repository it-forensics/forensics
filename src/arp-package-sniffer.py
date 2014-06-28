#!/usr/bin/python

# This tool is for educational use only!

# Description: Sniffs all arp packages in the LAN.
# Requirements: pcapy, getopt, impacket and root privileges

import sys
import getopt
import pcapy
from impacket.ImpactDecoder import EthDecoder

dev = "eth0"
# filter only arp packages
filter = "arp"
decoder = EthDecoder()

def handle_packet(hdr, data):
  """ prints the decoded packages
  :param hdr: package header information
  :param data: package data """
  print decoder.decode(data)

def usage():
  """ Prints usage information """
  print "{0} -i <dev> -f <pcap_filter>".format(sys.argv[0])

try:
  cmd_opts = "f:i:"
  opts, args = getopt.getopt(sys.argv[1:], cmd_opts)
except getopt.GetoptError:
  usage()

for opt in opts:
  if opt[0] == "-f":
    filter = opt[1]
  elif opt[0] == "-i":
    dev = opt[1]
  else:
    usage()

# open deivice in promisc mode
pcap = pcapy.open_live(dev, 1500, 0, 100)

# set pcap filter (filter arp packages)
pcap.setfilter(filter)

# start sniffing packages
pcap.loop(0, handle_packet)
