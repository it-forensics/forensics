#!/usr/bin/python

# This tool is for educational use only!

# Description: Scans ports 1 to 1025 on the destination host. Additionaly
# you can spoof the source ip.

# Requirements: scapy + root privilegues


import sys
from scapy.all import sr, IP, TCP

if len(sys.argv) < 2:
  print "{0} <host> [<spoofed_source_ip>]".format(sys.argv[0])
  sys.exit(1)

if len(sys.argv) == 3:
  packet = IP(dst=sys.argv[1], src=sys.argv[2])
else:
  packet = IP(dst=sys.argv[1])

packet /= TCP(dport=range(1, 1025), flags="S")

answered, unanswered = sr(packet, timeout=1)

res = {}

for packet in unanswered:
  res[packet.dport] = "filtered"

for (send, recv) in answered:
  if recv.getlayer("ICMP"):
    type = recv.getlayer("ICMP").type
    code = recv.getlayer("ICMP").code

    if code == 3 and type == 3:
      res[send.dport] = "closed"
    else:
      res[send.dport] = "Got ICMP with type {0} and code {1}".format(str(type), str(code))

  else:
    flags = recv.getlayer("TCP").sprintf("%flags%")

    if flags == "SA":
      res[send.dport] = "open"

    elif flags == "R" or flags == "RA":
      res[send.dport] = "closed"

    else:
      res[send.dport] = "Got packet with flags {0}".format(str(flags))

ports = res.keys()
ports.sort()

for port in ports:
  if res[port] != "closed":
    print "{0}: {1}".format(str(port), res[port])
