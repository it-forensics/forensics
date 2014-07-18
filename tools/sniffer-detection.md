# How to detect a network sniffer

** Local sniffer **

If a sniffer is running on your local machine, maybe some malware is sniffing
the network from your host, at least one network-interface has to run in
promisc mode. If no rootkit is locking this functionality, with
`ifconfig -a | grep PROMISC` or `cat /var/log/kern.log | grep promisc` you can
view if a network-interface is in promisc mode.

** Remote sniffer **

> Remote sniffer detection script [here](https://github.com/it-forensics/forensics/blob/master/src/sniffer-detection.py)

To detect sniffers in a local network, we could overload the network with
traffic and ping all hosts, the host with promisc mode enabled would, in theory,
respond slower, because he had to process all the packets. But this method
is not very relyable because, there would be a lot of traffic on the network and
the response delay could have different reasons.

The second possibility to detect if a host in the local network is in promisc
mode, is to send arp packets to an invalid mac address, the client with promisc
mode enabled would then respond to the packet.
