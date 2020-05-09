# ARP-Spoofer
  This is a program written in python 3.7 to spoof ARP table and become Man in the Middle between router and the target. This program sends an ARP packet to the target saying that this packet is sent from the router and spoofs the target to assign attacker’s MAC address with Router’s IP and does the same for Router‘s ARP table too.

### Syntax:
  ./arp-spoof \<ip-address-of-target\> <br>
  ./arp-spoof \<ip-address-of-target\> \<ip-address-of-router\>
  
### Features:
 * It provides help if the syntax or IP Address is wrong.
 ![alt-text](https://github.com/sawarni99/ARP-Spoofer/blob/master/images/invalid_ip.JPG)
 * This program automatically takes the MAC address of the router and target from previously assigned ARP tables. 
 * This program also assigns router’s IP address automatically if not specified.
 ![alt-text](https://github.com/sawarni99/ARP-Spoofer/blob/master/images/one_args.JPG)
 * This program also takes two arguments if there is a specific router’s IP.
 ![alt-text](https://github.com/sawarni99/ARP-Spoofer/blob/master/images/two_args.JPG)
 
### Download this arp-spoofer program with command:
  git clone https://github.com/sawarni99/ARP-Spoofer 
