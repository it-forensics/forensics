#!/usr/bin/python

# This tool is for educational use only!

# Description: Creates pcap-dump-files of the recorded network traffic.
# If a pcap-dump-file is given as parameter, the content will be printed
# to the screen.

# Requirements: pcapy, getopt, impacket and root privileges

import sys
import getopt
import pcapy
from impacket.ImpactDecoder import *
from impacket.ImpactPacket import *

dev = "eth0"
decoder = EthDecoder()
input_file = None
dump_file = "sniffer.pcap"

def usage():
  """ Prints usage information """
  print """{0}
    -i <dev>
    -r <input_file>
    -w <output_file>""".format(sys.argv[0])
  sys.exit(1)

def write_packet(hdr, data):
  """ prints the decoded packages
  :param hdr: package header information
  :param data: package data """
  print decoder.decode(data)
  dumper.dump(hdr, data)

def read_packet(hdr, data):
  ether = decoder.decode(data)
  if ether.get_ether_type() == IP.ethertype:
    l3hdr = ether.child()
    l4hdr = l3hdr.child()

    if l4hdr.protocol == ImpactPacket.TCP.protocol:
      print "[TCP] {0}:{1} -> {2}:{3}".format(
          l3hdr.get_ip_src(),
          l4hdr.get_th_sport(),
          l3hdr.get_ip_dst(),
          l4hdr.get_th_dport()
        )
    else:
      print "[UDP] {0}:{1} -> {2}:{3}".format(
          l3hdr.get_ip_src(),
          l4hdr.get_uh_sport(),
          l3hdr.get_ip_dst(),
          l4hdr.get_uh_dport()
        )

# parse parameter
try:
  cmd_opts = "i:r:w:"
  opts, args = getopt.getopt(sys.argv[1:], cmd_opts)
except getopt.GetoptError:
  usage()

for opt in opts:
  if opt[0] == "-w":
    dump_file = opt[1]
  elif opt[0] == "-i":
    dev = opt[1]
  elif opt[0] == "-r":
    input_file = opt[1]
  else:
    usage()

# start sniffing and write packet to pcap-dump-file
if input_file == None:
  pcap = pcapy.open_live(dev, 1500, 0, 100)
  dumper = pcap.dump_open(dump_file)
  pcap.loop(0, write_packet)

# read pcap dump file and print it
else:
  pcap = pcapy.open_offline(input_file)
  pcap.loop(0, read_packet)
